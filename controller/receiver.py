import socket
import json
import time
import UdpComms as U

server_address = 'd4:3b:04:97:da:5f' 
port = 5

# Initialization to add RFCOMM protocol to endpoint
serv = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True)

# Assigns a port for the server that listens to clients connecting to this port
serv.bind((server_address, port))
serv.listen()
prev_time = 0
while True:
    client, addr = serv.accept()
    while True:
        data = client.recv(4096)
        curr_time = time.time_ns()
        if not data: break 
        from_client_string = data.decode()

        #packet_time = (curr_time - prev_time) / (10**6)
        #prev_time = curr_time

        sock.SendData(from_client_string)
    client.close()
    print('client disconnected')
    break