from datetime import datetime
from tokenize import Ignore
import cv2
import pandas as pd

df1=pd.DataFrame(columns=["Start","End"])
first_frame=None
status_list=[None,None]
times_motionCapture=[]
vc=cv2.VideoCapture(0)
while True:
    check,frame=vc.read()
    status=0
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    threshold_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    threshold_frame=cv2.dilate(threshold_frame,None,iterations=2)
    
    (cnts,_)=cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for contours in cnts:
        if cv2.contourArea(contours)<10000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contours)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)
    
    status_list=status_list[-2:]
    
    if status_list[-1]==1 and status_list[-2]==0:
        times_motionCapture.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times_motionCapture.append(datetime.now())
        
    cv2.imshow("gray frame",gray)
    cv2.imshow("delta frame",delta_frame)
    cv2.imshow("threshold frame",threshold_frame)
    cv2.imshow("color frame",frame)
    
    print(gray)
    print(delta_frame)
    
    key=cv2.waitKey(1)
    if key ==ord('q'):
        if status==1:
            times_motionCapture.append(datetime.now())
        break
print(status_list)
print(times_motionCapture)

end = None
if len(times_motionCapture) % 2 != 0:
    end = len(times_motionCapture) -1
else:
    end = len(times_motionCapture)
 
for i in range(0, end, 2):
    df1 = df1.append({"Start": times_motionCapture[i], "End": times_motionCapture[i+1]}, ignore_index=True)
df1.to_csv("Times.csv")
vc.release()
cv2.destroyAllWindows()