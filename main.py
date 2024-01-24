import cv2
 
img = cv2.imread('img_files/boki.jpg')

img_size = cv2.resize(img, (0, 0), fx=2.0, fy=2.0)

cv2.imshow('img_boki', img_size)

cv2.waitKey(0)