import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    
    img_gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    cv2.imshow('Original',frame)
    edges = cv2.Canny(img_gray,40,240)
    cv2.imshow('Edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()