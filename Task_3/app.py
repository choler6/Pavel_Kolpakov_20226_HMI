import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from server import Server

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.status_label = QLabel()
        self.setCentralWidget(self.status_label)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    _ = Server(window)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
