import cv2
from PyQt5.QtWidgets import QFileDialog, QAction, QMainWindow, QWidget, QApplication
from PyQt5.QtGui import QWindow

def nothing ():
    pass

file = QFileDialog.getOpenFileName(QWidget, 'Open file', '/home')[0]
cap = cv2.VideoCapture(file)
cv2.namedWindow("image")
R = cv2.createTrackbar("R", "image", 0, 255, nothing)
G = cv2.createTrackbar("G", "image", 0, 255, nothing)
B = cv2.createTrackbar("B", "image", 0, 255, nothing)


while True:

    if cv2.waitKey(1) and 0xFF==ord("q"):
        break

    if cv2.waitKey(1) and 0xFF==ord("1"):
        print("key pressed 1")
        function(1)

    if cv2.waitKey(1) and 0xFF==ord("2"):
        print ("key pressed 2")
        function(2)

    if cv2.waitKey(1) and 0xFF==ord("3"):
        print('key pressed 3')
        function(3)

    if cv2.waitKey(1) and 0xFF==ord("4"):
        print('key pressed 4')
        function(4)


cv2.destroyAllWindows()