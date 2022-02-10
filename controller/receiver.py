import socket
import json
import time
import UdpComms as U
import subprocess
import tempfile

script = "findBTMac.bat"
run = subprocess.Popen(script, shell=True, stdout = subprocess.PIPE)
stdout, stderr = run.communicate()
print("Script returned with status code: " + str(run.returncode))

temp_dir = tempfile.gettempdir()
with open(temp_dir + '\mymac.txt', 'r') as file:
    filedata = file.read()

filedata = filedata.replace('-', ':')
print("Your bluetooth MAC address is: " + filedata)
file.close()
with open(temp_dir + '\mymac.txt', 'w') as file:
    file.write(filedata)
file.close()

server_address = filedata.strip() # change this to your computer's bluetooth MAC address
port = 5

# Initialization to add RFCOMM protocol to endpoint
serv = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) # bluetooth connection to raspberry PI
sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True) # communication with Unity
end_cv_sock = U.UdpComms(udpIP="127.0.0.1", portTX=8003, portRX=8004, enableRX=False, suppressWarnings=True) # communication with pose detection script

# Assigns a port for the server that listens to clients connecting to this port
serv.bind((server_address, port))
print("Awaiting controller connection...")
serv.listen()
prev_time = 0
prev_pose_data = 0
while True:
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
    client.close()
    print('client disconnected')
    break