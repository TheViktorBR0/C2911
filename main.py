import time
import cv2

time.sleep(2)
print("Connected to arduino...")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

cap_width = 800  # Set the desired width for the window
cap_height = 600  # Set the desired height for the window

cv2.namedWindow('img')  # Create a window

while True:
    ret, img = cap.read()
    if ret:
        img = cv2.resize(img, (cap_width, cap_height))  # Resize the captured frame

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
            center_x = x + w // 2  # Calculate the center of the face
            center_y = y + h // 2

            cv2.line(img, (center_x - 5, center_y), (center_x + 5, center_y), (0, 0, 255), 2)  # Horizontal line marker
            cv2.line(img, (center_x, center_y - 5), (center_x, center_y + 5), (0, 0, 255), 2)  # Vertical line marker

            print("Center coordinates of the face: ({}, {})".format(center_x, center_y))  # Print coordinates in console

        cv2.imshow('img', img)

        key = cv2.waitKey(20)
        if key == 27:
            print('Stop streaming')
            break

cap.release()
cv2.destroyAllWindows()
