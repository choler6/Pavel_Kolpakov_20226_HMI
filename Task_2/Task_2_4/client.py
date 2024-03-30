import socket
import time
import random
import data_pb2

temp = data_pb2.Temperature()
temp.temp_cel = 25


x = temp.SerializeToString()

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(x)
        temp.temp_cel = random.uniform(-30, 30)
        x = temp.SerializeToString()
        time.sleep(1)