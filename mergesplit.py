import cv2
import numpy as np

img=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\look.jpg")
img=cv2.resize(img,(600,500))
# #split eturns array of b g r in thus order
# b,g,r=cv2.split(img)
# # cv2.imshow("blue",b)
# # cv2.imshow("green",g)
# # cv2.imshow("red",r)
# cv2.imshow("origin",img)
# newimg=cv2.merge((r,g,b))
# new2=cv2.merge((g,r,b))
# cv2.imshow("new2",new2)
# cv2.imshow("new",newimg)
print(img.shape)
px=img[400,400]
print(px)
cv2.waitKey(0)
cv2.destroyAllWindows()
