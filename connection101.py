import cv2
camera="http://192.168.29.127:8080/video"
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(camera)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter(r"C:\Users\KIIT0001\OneDrive\Desktop\phone.mp4",fourcc,20.0,(640,480))
while (cap.isOpened()):
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    cv2.imshow("frsme",frame)
    output.write(frame)
    k=cv2.waitKey(25)
    if k==ord("q"):
        break
cap.release()
output.release()
cv2.destroyAllWindows()
