import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, color_img = cap.read()
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img)
    for (x, y, w, h) in faces:
        cv2.rectangle(color_img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    eyes = eye_cascade.detectMultiScale(gray_img)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(color_img, (ex, ey), (ex+ew, ey+eh), ( 0, 255, 0), 2)

    cv2.imshow('img', color_img)
    k = cv2.waitKey(30) & 0xff
    if k == 113:
        break

cap.release()
cv2.destroyAllWindows()