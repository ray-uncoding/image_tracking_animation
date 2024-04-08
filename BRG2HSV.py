# 如果需要做顏色辨識, 可以藉由這段程式碼找到顏色域值

import cv2
import numpy as np

def empty(v):
    pass


#cap = cv2.VideoCapture(1)

#img = cv2.imread('img_files/orange_rectangle (3).png')  # 取得圖片
img = cv2.imread('img_files/green.png')  # 取得圖片
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # 縮放
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 使用 cv2.WINDOW_NORMAL 以允許視窗大小的調整
cv2.namedWindow('TrackBar', cv2.WINDOW_NORMAL)
cv2.resizeWindow('TrackBar', 640, 320)  # 調整視窗大小

cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

while True:
    #ret, img = cap.read()
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBar")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(HSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.waitKey(1)

    #cv2.imshow('img_boki', img)
    #cv2.imshow('HSV', HSV)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
