import time
import cv2

time.sleep(2)
print("Connected to arduino...")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

cap_width = 1280
cap_height = 720

while True:
    ret, img = cap.read()
    cv2.resizeWindow('img', cap_width, cap_height)
    cv2.line(img, (cap_width, cap_height//2, (0, cap_height//2), (0, 255, 0), 1))
    cv2.line(img, (cap_width//2, 0), (cap_width//2, cap_height), (0.255, 0), 1)
    cv2.circle(img, (cap_width//2, cap_height//2), 5, (255, 255, 255), -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGT2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)
    