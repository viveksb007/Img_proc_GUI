from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Img_Proc_Gui(QWidget):
    def __init__(self, parent=None):
        super(Img_Proc_Gui, self).__init__(parent)
        btn_process_img = QPushButton("Process Image")
        btn_quit = QPushButton("Quit")
        btn_quit.clicked.connect(self.quit_clicked)
        hbox_btn = QHBoxLayout()
        hbox_btn.addWidget(btn_process_img)
        hbox_btn.addWidget(btn_quit)

        hbox_address = QHBoxLayout()
        address = QLineEdit()
        hbox_address.addWidget(address)
        btn_img_explorer = QPushButton('Open Image')
        hbox_address.addWidget(btn_img_explorer)

        hbox_size = QHBoxLayout()
        label_width = QLabel('Width :')
        label_height = QLabel('Height :')
        et_width = QLineEdit()
        et_height = QLineEdit()
        hbox_size.addWidget(label_width)
        hbox_size.addWidget(et_width)
        hbox_size.addWidget(label_height)
        hbox_size.addWidget(et_height)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_address)
        vbox.addLayout(hbox_size)
        vbox.addLayout(hbox_btn)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Image Processing')
        self.setLayout(vbox)

    @pyqtSlot()
    def quit_clicked(self):
        print("Sayonaara!!")
        self.close()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Img_Proc_Gui()
    screen.show()



    sys.exit(app.exec_())
