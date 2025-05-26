import cv2
import numpy as np
# img=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\vision.jpg")
img=np.zeros([500,500,3],np.uint8)*255
img=cv2.resize(img,(600,720))
img=cv2.line(img,(0,0),(200,200),(154,92,424),8)
cv2.imshow("line",img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()