#to find the color of whereever the mouse is and as welll as pixels
import cv2
import numpy as np

def draw(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        text=". "+str(x)+", " +str(y)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(10,240,247),1)
        #gives pixel coordinates
    if event==cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        text="BGR= "+str(b)+", "+str(g)+", "+str(r)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(152,255,130),1)
        #gives color  the pixel coordinate

cv2.namedWindow("picture")
cv2.setMouseCallback("picture",draw)
# img=np.zeros([500,500,3],np.uint8)*255
img=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\vision.jpg")

while True:
    cv2.imshow("picture",img)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cv2.destroyAllWindows()