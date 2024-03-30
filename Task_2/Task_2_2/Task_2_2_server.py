import socket
import pickle

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected ', addr)
        while True:
            data = conn.recv(4096)
            if not data:
                break
            x = pickle.loads(data)
            print(x)