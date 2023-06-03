import cv2

image_path = 'cat.jpg'

cat_face_cascade = cv2.CascadeClassifire('haarcascade_frontalcatface_extended.xml')

image = cv2.imread(image_path)

cv2.imshow('Cat', image)
cv2.waitKey()