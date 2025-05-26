import cv2
cap=cv2.VideoCapture(r"C:\Users\KIIT0001\Downloads\legendary-first-appearance-intro-scene-pirates-of-the-caribbean-full-hd---captain-jack-sparrow.mp4")
res,frame=cap.read()
count=0
while True:
    cv2.imwrite(r"C:\Users\KIIT0001\OneDrive\Desktop\neww\frame%d.jpg"%count,frame)
    cap.set(cv2.CAP_PROP_POS_MSEC,(100*count))#position in ms here 10 frames per sec 
    res,frame=cap.read()
    print(count)
    cv2.imshow("video",frame)
    count+=1
    k=cv2.waitKey(1)
    if k==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()