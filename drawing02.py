#drawing function in videos
import cv2
import datetime
cap=cv2.VideoCapture(r"C:\Users\KIIT0001\Downloads\legendary-first-appearance-intro-scene-pirates-of-the-caribbean-full-hd---captain-jack-sparrow.mp4")
w=cap.get(3)# 3means width here and 4 means heght itis what it is
h=cap.get(4)
while (cap.isOpened()):
    ref,frame=cap.read()
    text= "height "+str(h)+"width "+str(w)
    frame=cv2.putText(frame,text,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    text2=datetime.datetime.now()
    frame=cv2.putText(frame,str(text2),(10,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow("Video",frame)
    k=cv2.waitKey(30)
    if k==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()