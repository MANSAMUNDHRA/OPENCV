from calendar import c
import cv2
# cap=cv2.VideoCapture(r"C:\Users\KIIT0001\Downloads\legendary-first-appearance-intro-scene-pirates-of-the-caribbean-full-hd---captain-jack-sparrow.mp4")
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter(r"C:\Users\KIIT0001\OneDrive\Desktop\video.avi",fourcc,20.0,(640,480))
while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow("frame",frame)
    output.write(frame)
    k = cv2.waitKey(25)
    if k==ord("q"):
        break
cap.release()
output.release()
cv2.destroyAllWindows()