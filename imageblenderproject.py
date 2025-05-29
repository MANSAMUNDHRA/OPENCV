import numpy as np
import cv2

img1=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\thor.jpeg")
img1=cv2.resize(img1,(400,400))
img2=cv2.imread(r"C:\Users\KIIT0001\OneDrive\Desktop\thor2.jpeg")
img2=cv2.resize(img2,(400,400))
cv2.namedWindow("blender")

def blend():
    pass

change=cv2.createTrackbar("range","blender",0,100,blend)
on_off=cv2.createTrackbar("on/off","blender",0,1,blend)

img=np.zeros((400,400,3),np.uint8)*255
while True:
    n=cv2.getTrackbarPos("range","blender")
    s=cv2.getTrackbarPos("on/off","blender")
    if s==0:
        ahh=img[:]
    else:
        ahh=cv2.addWeighted(img1,n/100,img2,1-n/100,0)
        ahh=cv2.putText(ahh,str(n), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("ahh",ahh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()