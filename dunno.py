import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import sys
import cv2

'''
img = cv2.imread('11.png')
cv2.imshow('yo',img)
'''


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Process Image", self)
        btn1.move(20,10)
        btn1.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage('Complete Program First')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
