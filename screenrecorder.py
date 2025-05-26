import cv2
import pyautogui as p
import numpy as np

#resolution:
rs=p.size()

#file where we store the recording
stored = r"C:\Users\KIIT0001\OneDrive\Desktop\new.avi"

fps=25.0

fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter(stored,fourcc,fps,rs)

#create recording moduleq
cv2.namedWindow("Live_recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_recording", (640, 480))

while True:
    img=p.screenshot()
    frame=np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    # cv2.imshow("Live_recording",frame)
    #line causing mirror live_recording window
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
output.release()
cv2.destroyAllWindows()
