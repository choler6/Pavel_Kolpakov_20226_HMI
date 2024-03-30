import socket
import time

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    txt = 'I`m connected to server!'
    x = txt.encode()

    while True:
        s.sendall(x)
        time.sleep(1)
