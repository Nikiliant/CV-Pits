import cv2

def nothing ():
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("image")
R = cv2.createTrackbar("R","image",0,255, nothing)

while True:

    if 0xFF==ord("q"):
        break


cv2.destroyAllWindows()