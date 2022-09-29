import cv2
import numpy as np

# Declaring capture window size
cap=cv2.VideoCapture(0)
cap.set(3,64)
cap.set(4,48)
cap.set(10,130)

# Function to read video via cam
while True:
    success,img=cap.read()
    cv2.imshow("INPUT CAM",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
