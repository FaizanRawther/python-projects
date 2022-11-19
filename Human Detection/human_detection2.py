import cv2
video_Capture=cv2.VideoCapture("video.avi")
human_cascade=cv2.CascadeClassifier("fullbody.xml")
while (True):
    #capture frame by frame
    check,frame=video_Capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    humans=human_cascade.detectMultiScale(gray,1.9,1)
    c=1
    for (x,y,w,h) in humans:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,f'P{c}',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
        c=c+1
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video_Capture.release()
cv2.destroyAllWindows()
