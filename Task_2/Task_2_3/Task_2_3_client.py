import socket
import time
import data_pb2

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = data_pb2.MyData()
    data.message = 'I`m connected to server!'
    data.number = 123
    data.status = True

    while True:
        serialized_data = data.SerializeToString()
        s.sendall(serialized_data)
        time.sleep(1)