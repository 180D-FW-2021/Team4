import socket
import json
import time
import UdpComms as U

server_address = '5c:fb:3a:65:d7:80' # change this to your computer's bluetooth MAC address
port = 5

# Initialization to add RFCOMM protocol to endpoint
serv = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True)
end_cv_sock = U.UdpComms(udpIP="127.0.0.1", portTX=8003, portRX=8004, enableRX=False, suppressWarnings=True)

# Assigns a port for the server that listens to clients connecting to this port
serv.bind((server_address, port))
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