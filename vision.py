import cv2
img1=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\vision.jpg",1)
img1=cv2.resize(img1,(1290,600))
cv2.imshow("original",img1)
k=cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite(r"C:\Users\KIIT0001\OneDrive\Desktop\hope.png",img1) 
else:
    cv2.destroyAllWindows    

from PIL import Image
 
img=Image.open(r"C:\Users\KIIT0001\OneDrive\Desktop\hope.png")
img.save(r"C:\Users\KIIT0001\OneDrive\Desktop\hopeful.pdf")