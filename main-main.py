import cv2 as cv
import time
import serial

cap = cv.VideoCapture(0)
eyeCascade = eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
arduino = serial.Serial(port='COM11', baudrate=115200, timeout=.1)

def findEyes(img, EyeCascade):
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    eyes = EyeCascade.detectMultiScale(grayImg)
    if len(eyes) == 0:
        return 0
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(img, (ex, ey), (ex+ew, ey+eh), ( 0, 255, 0), 2)

def returnArduinoData():
    arduino.write(bytes('0', 'utf-8'))
    time.sleep(0.05)
    data = arduino.read()
    return data

while True:
    success, img = cap.read()
    if findEyes(img, eyeCascade) == 0:
        returnArduinoData()

    cv.imshow('Face Detector', img)
    cv.waitKey(1)
