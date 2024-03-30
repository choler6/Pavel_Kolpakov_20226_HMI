from PySide6.QtNetwork import QTcpServer
import data_pb2

t = data_pb2.Temperature()


class Server(QTcpServer):
    def __init__(self, window, parent=None):
        super().__init__(parent)
        self.mainWindow = window
        self.newConnection.connect(self.handleConnection)
        self.listen(port = 12345)

    def handleConnection(self):
        client_socket = self.nextPendingConnection()
        print(client_socket)
        client_socket.readyRead.connect(self.readData)

    def readData(self):
        client_socket = self.sender()  # ReadAll
        b = bytes(client_socket.readAll())
        t.ParseFromString(b)
        self.mainWindow.label.setText(('Temperature: ' + str(t.temp_cel)[0:2]))
