import cv2
img=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\look.jpg")
img=cv2.resize(img,(1024,690))
#1st:550,80 2nd:640,205
roi=img[80:205,550:640]
img[80:205,641:731]=roi
# cv2.imshow("roi",roi)
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()