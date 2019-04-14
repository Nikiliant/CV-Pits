import cv2, os, skimage, numpy
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMainWindow
class MyWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.file = None
        self.NamesOfTypes = ["1", "2", "3", "4"]
        self.resize(400, 150)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 400, 150))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Выходной каталог")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("...")
        self.pushButton.clicked.connect(lambda: self.setFile())
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("...")
        self.pushButton_2.clicked.connect(lambda: self.setFolder())
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.label.setText("Входной файл")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("Запуск")
        self.pushButton_3.clicked.connect(lambda: self.Cv(self.lineEdit.text()))
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 2)


    def ImageFunction (self, Image, Txt):
        ImgTxt = [Image, Txt]
        self.file.writelines(str(ImgTxt))
        self.file.write(str('\r'))
        return 0

    def setFolder (self):
        self.lineEdit_2.setText(QFileDialog.getExistingDirectory(self, "Выбор каталога", "~/"))
        return 0

    def setFile(self):
        self.lineEdit.setText(QFileDialog.getOpenFileName(self, "Открытие файла", "~/")[0])
        return 0

    def createFile(self):
        path = self.lineEdit_2.text()
        filename = self.writeAFile(path)
        self.file = open(filename, 'a')
        return 0

    def writeAFile(self, dir):
        count = 0
        listoffiles = os.listdir(dir)
        for a in listoffiles:
            if ('dataset' in a)==True:
                count += 1

        if count == 0:
            fi = 'dataset_1'
        else:
            fi = 'dataset_'+str(count+1)


        return fi

    def Cv (self, f):
        self.createFile()
        if f[0] != "":
            cap = cv2.VideoCapture(f[0])
            img = cap.read()
            cv2.namedWindow("image")
            while True:
                k = chr(cv2.waitKey())
                if k=='q':
                    break

                if k=='1':
                    MyWindow.ImageFunction(self, img, self.NamesOfTypes[0])
                    print("key pressed 1")

                if k=='2':
                    MyWindow.ImageFunction(self, img, self.NamesOfTypes[1])
                    print("key pressed 2")

                if k=='3':
                    MyWindow.ImageFunction(self, img, self.NamesOfTypes[2])
                    print('key pressed 3')

                if k=='4':
                    MyWindow.ImageFunction(self, img, self.NamesOfTypes[3])
                    print('key pressed 4')
            cv2.destroyAllWindows()
            self.file.close()


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())