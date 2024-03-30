import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from server import Server


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task 2_4")
        self.label = QLabel()
        self.setCentralWidget(self.label)
        self.label.setText('Waiting for connection...')


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    _ = Server(window)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
