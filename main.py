import cv2 as cv
from cvzone.FaceDetectionModule import FaceDetector
import time
import serial

cap = cv.VideoCapture(0)
detector = FaceDetector()
eyeCascade = eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
serialcomm = serial.Serial(port='COM4', baudrate='115200', timeout=.1)

def findEyes(img, EyeCascade):
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    eyes = EyeCascade.detectMultiScale(grayImg)
    if len(eyes) == 0:
        return 0
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(img, (ex, ey), (ex+ew, ey+eh), ( 0, 255, 0), 2)

while True:
    success, img = cap.read()
    img, bBoxes = detector.findFaces(img)
    if findEyes(img, eyeCascade) == 0:
        i = "onn"
        serialcomm.write(i.encode())
        
    if findEyes(img, eyeCascade) != 0:
        i = "off"
        serialcomm.write(i.encode())

    cv.imshow('Face Detector', img)
    cv.waitKey(1)
