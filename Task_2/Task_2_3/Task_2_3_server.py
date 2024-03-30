import socket
import data_pb2

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
            received_data = data_pb2.MyData()
            received_data.ParseFromString(data)
            print(received_data.message)
            print(received_data.number)
            print(received_data.status)