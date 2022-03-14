import socket
import json
import UdpComms as U
import tempfile
import sys
import argparse
import threading
import time

sys.path.append("../")
import PoseModule as PM

# TODO: Add command line argument to run without initiating posemodule
parser = argparse.ArgumentParser(description='Launch without pose module')
parser.add_argument('--poseoff', action='store_true')
parser.add_argument('-controlleroff', action='store_true')

args = vars(parser.parse_args())
temp_dir = tempfile.gettempdir()
try:
    with open(temp_dir + '/freeride_setup/mymac.txt', 'r') as file:
        filedata = file.read()
except OSError as e:
    print("MAC address file not found. Have you run the first time setup script?")
    exit()

# t1 = threading.Thread(target=PM.main, daemon=True)
# t1.start()

print("Your bluetooth MAC address is: " + filedata)
file.close()

server_address = filedata.strip() # change this to your computer's bluetooth MAC address
port = 5

# Initialization to add RFCOMM protocol to endpoint
serv = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) # bluetooth connection to raspberry PI
sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True) # communication with Unity
end_cv_sock = U.UdpComms(udpIP="127.0.0.1", portTX=8003, portRX=8004, enableRX=False, suppressWarnings=True) # communication with pose detection script

# Start pose detection script
if not (args['poseoff']):
    t1 = threading.Thread(target=PM.main, daemon=True)
    t1.start()

# Assigns a port for the server that listens to clients connecting to this port
serv.bind((server_address, port))
serv.settimeout(0.1)
print("Awaiting controller connection...")
serv.listen()
prev_time = 0
prev_pose_data = 0
while True:
    try:
        client, addr = serv.accept()
        while True:
            bt_data = client.recv(3, socket.MSG_WAITALL) # ensure that entire output from IMU script is received
            if not bt_data: break 
            from_bt_string = bt_data.decode()

            pose_data = sock.ReadReceivedData()
            if pose_data != None:
                prev_pose_data = pose_data

            output_obj = {
                "bt_data": int(bt_data),
                "pose_data": int(prev_pose_data)
            }

            output_obj_str = json.dumps(output_obj)
            sock.SendData(output_obj_str)
            print(output_obj_str)

            bt_data = None
    except socket.timeout as e:
        err = e.args[0]
        print(e)
        continue
    except socket.error as e:
        err = e.args[0]
        print(e)
        exit(1)

    # while True:
    #     bt_data = client.recv(3, socket.MSG_WAITALL) # ensure that entire output from IMU script is received
    #     if not bt_data: break 
    #     from_bt_string = bt_data.decode()

    #     pose_data = sock.ReadReceivedData()
    #     if pose_data != None:
    #         prev_pose_data = pose_data

    #     output_obj = {
    #         "bt_data": int(bt_data),
    #         "pose_data": int(prev_pose_data)
    #     }

    #     output_obj_str = json.dumps(output_obj)
    #     sock.SendData(output_obj_str)
    #     print(output_obj_str)

    #     bt_data = None
    #client.close()
    print('client disconnected')
    break