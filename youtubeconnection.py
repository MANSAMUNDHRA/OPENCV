import cv2
import pafy
# pafy.set_backend("internal")

url = "https://www.youtube.com/watch?v=dvdrCPr3gDQ"
data = pafy.new(url)
data = data.getbest(preftype="mp4")

cap = cv2.VideoCapture(data.url)  

while (cap.isOpened()):
    ref, frame = cap.read()
    if not ref:
        break
    cv2.imshow("youtube", frame)
    k = cv2.waitKey(25)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
