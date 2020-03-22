import numpy as np
import cv2

# Select capture from a source(Replace 0 with video file for debugging purposes if no webcam available)
capture = cv2.VideoCapture(0)

# Capture video input(Enter q to stop capture)
while(True):
    ret, frame = capture.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', grayscale)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture
capture.release()
cv2.destroyAllWindows()
