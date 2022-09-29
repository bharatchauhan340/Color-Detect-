import cv2
import numpy as np

framew=64
frameh=48
cap=cv2.VideoCapture(0)
cap.set(3,framew)
cap.set(4,frameh)
cap.set(10,130)

# Making color array for three different colors [orange purple green] ,[133,56,0,159,156,255],[57,76,0,100,255,255]
mycolors=[[0, 100, 20, 10, 255, 255]]

def findcolor(img,mycolors):
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for mc in mycolors:
        lower= np.array(mc[0:3]) #lower range of HSV
        upper= np.array(mc[3:6]) #Upper range of HSV
        mask=cv2.inRange(imgHSV,lower,upper)
        imask = mask > 0
        orange = np.zeros_like(img, np.uint8) #np.uint8 is unsigned integer and it consists of 8 bits
        # np.zeroes_like Return an array of zeros with the same shape and type as a given array
        orange[imask] = img[imask]  # changing values>0 to original image values (Value of Black is 0 in HSV)
        cv2.imshow("ORANGE DETECTED",orange)

while True :
    success,img=cap.read()
    findcolor(img,mycolors)
    cv2.imshow("INPUT CAM",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Photo Read
