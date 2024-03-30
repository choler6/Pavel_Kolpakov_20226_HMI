from PySide6.QtNetwork import QTcpServer
from PySide6.QtGui import QPixmap
import bytes_pb2

t = bytes_pb2.my_image()

class Server(QTcpServer):
    def __init__(self, window, parent=None):
        super().__init__(parent)

        self.mainWindow = window

        self._bytes = b''
        self._amount = 0
        self.newConnection.connect(self.handleConnection)
        self.listen(port = 12345)

    def handleConnection(self):
        client_socket = self.nextPendingConnection()
        print(client_socket)
        client_socket.readyRead.connect(self.readData)

    def readData(self):
        client_socket = self.sender() # ReadAll
        if(self._amount == 0):
            self._bytes = bytes(client_socket.read(4))
            self._amount = int.from_bytes(self._bytes)
            self._bytes = b''

        self._bytes += bytes(client_socket.read(self._amount - len(self._bytes)))
        if(self._amount - len(self._bytes) == 0):
            a = t.ParseFromString(self._bytes)
            pm = QPixmap()
            pm.loadFromData(t.image)
            self.mainWindow.status_label.setPixmap(pm)
            self._amount = 0