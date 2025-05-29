import cv2
import numpy as np
img1=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\thor.jpeg")
img1=cv2.resize(img1,(640,480))
img2=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\thor2.jpeg")
img2=cv2.resize(img2,(640,480))
# result=img1+img2
result=cv2.add(img1,img2)
cv2.imshow("result",result)
cv2.imshow("thor2",img2)
cv2.imshow("thor1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()