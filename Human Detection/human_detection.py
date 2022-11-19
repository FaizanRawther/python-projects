import cv2,time
import numpy as np
first_frame=None
video=cv2.VideoCapture('video.avi')
while (True):
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    thres_frame=cv2.threshold(delta_frame,25,255,cv2.THRESH_BINARY)[1]
    thres_frame=cv2.dilate(thres_frame,None,iterations=2)
    (cnts,_)=cv2.findContours(thres_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    c=1
    for countours in cnts:
        if cv2.contourArea(countours)<2000:
            continue
        (x,y,h,w)=cv2.boundingRect(countours)
        cv2.rectangle(frame,(x,y),(x+h,y+w),(0,255,0),1)
        cv2.putText(frame,f'P{c}',(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
        c=c+1
    
    cv2.imshow('gray frame',gray)
    cv2.imshow('delta frame',delta_frame)
    cv2.imshow('threshold frame',thres_frame)
    cv2.imshow('Color frame',frame)
    
    key=cv2.waitKey(1)
    print(gray)
    print(delta_frame)
    if key==ord('q'):
        break
video.release()
cv2.destroyAllWindows()