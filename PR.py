import cv2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow

class MyWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        FileDialog = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print(FileDialog)
        self.Cv(FileDialog)


    def ImageFunction1 (self):

        pass

    def Cv (self, f):
        if f[0] != "":
            cap = cv2.VideoCapture(f[0])
            cv2.namedWindow("image")
            while True:
                if cv2.waitKey(1) and 0xFF == ord("q"):
                    break

                if cv2.waitKey(1) and 0xFF == ord("1"):
                    print("key pressed 1")

                if cv2.waitKey(1) and 0xFF == ord("2"):
                    print("key pressed 2")

                if cv2.waitKey(1) and 0xFF == ord("3"):
                    print('key pressed 3')

                if cv2.waitKey(1) and 0xFF == ord("4"):
                    print('key pressed 4')
            cv2.destroyAllWindows()

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())