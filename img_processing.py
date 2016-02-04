from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2


class Img_Proc_Gui(QWidget):
    def __init__(self, parent=None):
        super(Img_Proc_Gui, self).__init__(parent)
        btn_process_img = QPushButton("Process Image")
        #calling for INPUT
        btn_process_img.clicked.connect(self.getInput)

        btn_quit = QPushButton("Quit")
        btn_quit.clicked.connect(self.quit_clicked)
        hbox_btn = QHBoxLayout()
        hbox_btn.addWidget(btn_process_img)
        hbox_btn.addWidget(btn_quit)

        hbox_address = QHBoxLayout()
        self.address = QLineEdit()
        hbox_address.addWidget(self.address)
        btn_img_explorer = QPushButton('Open Image')
        hbox_address.addWidget(btn_img_explorer)

        btn_img_explorer.clicked.connect(self.open)

        hbox_size = QHBoxLayout()
        label_width = QLabel('Width :')
        label_height = QLabel('Height :')
        self.et_width = QLineEdit()
        self.et_height = QLineEdit()
        hbox_size.addWidget(label_width)
        hbox_size.addWidget(self.et_width)
        hbox_size.addWidget(label_height)
        hbox_size.addWidget(self.et_height)

        hbox_save = QHBoxLayout()
        self.address_save = QLineEdit()
        hbox_save.addWidget(self.address_save)
        self.btn_save = QPushButton('Save Image')
        hbox_save.addWidget(self.btn_save)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_address)
        vbox.addLayout(hbox_size)
        vbox.addLayout(hbox_btn)
        vbox.addLayout(hbox_save)

        self.setGeometry(400,300,400,200)
        self.setWindowTitle('Image Processing')
        self.setLayout(vbox)

    #@pyqtSlot()
    def quit_clicked(self):
        print("Sayonaara!!")
        cv2.destroyAllWindows()
        self.close()

   # @pyqtSlot()
    def open(self):
        fileName = QFileDialog.getOpenFileName(self,'openFile')
        self.address.setText(fileName[0])
        self.showImage(fileName[0])
        #print(fileName)

    def showImage(self,address):
        img = cv2.imread(address)
        cv2.imshow('Yo',img)

    def getInput(self):
        self.req_height = self.et_height.text()
        self.req_width = self.et_width.text()
        if self.req_width != '' and self.req_height != '':
            self.ready = True
        else:
            self.ready =  False

        if self.ready is False :
            QMessageBox.about(self,'Error','Fill parameters to process')
        elif self.address.text() is '':
            QMessageBox.about(self,'Error','Select Image to process')
        else:
            self.req_img = self.process_img(cv2.imread(self.address.text()))
            cv2.imshow("req_img",self.req_img)

        #print(self.req_height,self.req_width)

    def process_img(self,imgtoproc):
        return cv2.resize(imgtoproc, (int(self.req_width),int(self.req_height)))





if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Img_Proc_Gui()
    screen.show()
    sys.exit(app.exec_())
