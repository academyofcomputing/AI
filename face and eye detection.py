import cv2
 
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
 
 
### download these two files and put them in the same directory as your python file
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
 
 
face_cascade = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')
 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
 
cap = cv2.VideoCapture(1) ### you may need to change this to 0 depending on your set-up
 
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
 
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
 
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # Esc key http://www.asciitable.com/ (Dec column)
        break
 
cap.release()
cv2.destroyAllWindows()
