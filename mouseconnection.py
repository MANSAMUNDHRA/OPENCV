import cv2
import numpy as np

def draw(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),5)
    elif event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+100,y+100),(0,255,0),5)


cv2.namedWindow( winname="Mouse")
cv2.setMouseCallback("Mouse",draw) 
img=np.zeros([500,500,3],np.uint8)*255
while True:
    cv2.imshow("Mouse",img)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cv2.destroyAllWindows()        
