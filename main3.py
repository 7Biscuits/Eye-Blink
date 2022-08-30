import numpy as np
import cv2 as cv
import threading 

def findEyes(img, eyeCascade):
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    eyes = eyeCascade.detectMultiScale(grayImg)
    if len(eyes) == 0:
        return 'EyesNotFound'
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(img, (ex, ey), (ex+ew, ey+eh), ( 0, 255, 0), 2)

def PutText(img):
    cv.putText(img, "Eyes Closed", (50, 50), cv.FONT_HERSHEY_PLAIN, 3,(0,255,0),2)

def main():
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
    cam = cv.VideoCapture(0)

    while True:
        _ret, img = cam.read()

        findEyes(img, eye_cascade)
        if (findEyes(img, eye_cascade) == 'EyesNotFound'):
            t = threading.Timer(5, PutText(img))
            t.start()

        cv.imshow('Eye detection', img)

        if cv.waitKey(5) == 27:
            break
        
if __name__ == '__main__':
    main()
    cv.destroyAllWindows()
