import cv2
import numpy as np
import pyautogui
import math

def start_opencv():
    nose_cascade = cv2.CascadeClassifier('classifiers/haarcascade_mcs_nose.xml')

    if nose_cascade.empty():
        raise IOError('Unable to load the nose cascade classifier xml file')


    pyautogui.FAILSAFE = False
    SCREEN_X, SCREEN_Y = pyautogui.size()

    cap = cv2.VideoCapture(0)
    ds_factor = 0.5

    settings = open("settings.txt", "r")
    speed = int(settings.read())

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        CAMERA_X, CAMERA_Y, channels = frame.shape
    
        nose_rects = nose_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in nose_rects:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
            c_x = x
            c_y = y
            c_x = x * (SCREEN_X / CAMERA_X) + speed
            c_y = y * (SCREEN_Y / CAMERA_Y) + speed
                
            pyautogui.moveTo(c_x,c_y)

        cv2.imshow('Nose Detector', frame)

        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    