import numpy as np
import cv2 as cv

def findFace(img, faceCascade):
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=3, flags=cv.CASCADE_SCALE_IMAGE)

    myFaceListC = []
    myFaceListArea = []

    if len(faces) == 0:
        return img, [[0, 0], 0]

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv.circle(img, (cx, cy), 5, (0, 255, 0), cv.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)
        if len(myFaceListArea) != 0:
            i = myFaceListArea.index(max(myFaceListArea))
            return img, [myFaceListC[i], myFaceListArea[i]]
        else:
            return img, [[0, 0], 0]

def findEyes(img, eyeCascade):
    grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    eyes = eyeCascade.detectMultiScale(grayImg)
    if len(eyes) == 0:
        
        print('Eyes not found')
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(img, (ex, ey), (ex+ew, ey+eh), ( 0, 255, 0), 2)

def main():
    cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
    cam = cv.VideoCapture(0)

    while True:
        _ret, img = cam.read()
        img, info = findFace(img, cascade)
        findEyes(img, eye_cascade)
        cv.imshow('facedetect', img)

        if cv.waitKey(5) == 27:
            break

    print('Done')

if __name__ == '__main__':
    main()
    cv.destroyAllWindows()