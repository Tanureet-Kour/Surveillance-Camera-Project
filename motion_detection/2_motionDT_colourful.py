# 2
# MOTION DETECTION (using two frames), colourful

import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret , frame1 = cam.read()
    ret , frame2 = cam.read()
    diff         = cv2.absdiff(frame1,frame2)
    
    if cv2.waitKey(10)== ord("q"):
        break
    
    cv2.imshow("SURVEILLANCE CAMERA PROJECT", diff)


