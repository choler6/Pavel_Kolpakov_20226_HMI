import socket
import time
import pickle

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = {'message': 'I`m connected to server!', 'number': 123, 'status': True}
    serialized_data = pickle.dumps(data)

    while True:
        s.sendall(serialized_data)
        time.sleep(1)
