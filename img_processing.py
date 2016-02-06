from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2


class Img_Proc_Gui(QWidget):
    def __init__(self, parent=None):
        super(Img_Proc_Gui, self).__init__(parent)
        self.img_processed = False
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

        hbox_colorscale = QHBoxLayout()
        color_scale = QLabel('Color Scale :')
        self.Grey_scale = QRadioButton('Grey',self)
        self.Hsv = QRadioButton('HSV ',self)
        hbox_colorscale.addWidget(color_scale)
        hbox_colorscale.addWidget(self.Grey_scale)
        hbox_colorscale.addWidget(self.Hsv)

        hbox_save = QHBoxLayout()
        self.address_save = QLineEdit()
        hbox_save.addWidget(self.address_save)
        self.btn_save = QPushButton('Save Image')
        self.btn_save.clicked.connect(self.save)
        hbox_save.addWidget(self.btn_save)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox_address)
        vbox.addLayout(hbox_size)
        vbox.addLayout(hbox_colorscale)
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

    def save(self):
        if self.img_processed:
            saveFile = QFileDialog.getSaveFileName(self,'saveFile')
            self.address_save.setText(saveFile[0])
            if saveFile[0] != '':
                cv2.imwrite(str(self.address_save.text()),self.req_img)
        else:
            QMessageBox.about(self,'Suggestion','Do Something')


    def showImage(self,address):
        img = cv2.imread(address)
        cv2.imshow('Yo',img)

    def getInput(self):
        self.req_height = self.et_height.text()
        self.req_width = self.et_width.text()
        if self.req_width != '' and self.req_height != '':
            self.ready = True
            self.img_processed = True
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
        if self.Grey_scale.isChecked():
            imgtoproc = cv2.cvtColor(imgtoproc,cv2.COLOR_BGR2GRAY)
        elif self.Hsv.isChecked():
            imgtoproc = cv2.cvtColor(imgtoproc,cv2.COLOR_BGR2HSV)

        return cv2.resize(imgtoproc, (int(self.req_width),int(self.req_height)))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Img_Proc_Gui()
    screen.show()
    sys.exit(app.exec_())
