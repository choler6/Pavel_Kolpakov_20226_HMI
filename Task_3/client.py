import cv2
import socket
import bytes_pb2
import time


def send_video_frames(video_path, host, port):
    t = bytes_pb2.my_image()
    vid = cv2.VideoCapture(video_path)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            ret, frame = vid.read()
            if not ret:
                break

            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                continue

            t.image = bytes(buffer)
            x = t.SerializeToString()
            message = len(x).to_bytes(4, byteorder='big') + x
            s.sendall(message)
            time.sleep(0.033)

    vid.release()


if __name__ == "__main__":
    send_video_frames('tik.mp4', 'localhost', 12345)
