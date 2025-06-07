import cv2
import numpy as np

frame=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\colorful.jpg")
while True:
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    upper=np.array([100, 150, 0])
    lower=np.array([140, 255, 255])
    masking=cv2.inRange(hsv,upper,lower)

    final=cv2.bitwise_and(frame,frame,mask=masking)
    cv2.imshow("masking",masking)
    cv2.imshow("final",final)
    cv2.imshow("original",frame)
    
    k=cv2.waitKey(1)
    if k==ord('q'):
        break

cv2.destroyAllWindows()

