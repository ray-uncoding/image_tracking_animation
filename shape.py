import cv2
 
img = cv2.imread('img_files/boki.jpg')  #讀圖
img = cv2.resize(img, (0, 0), fx=2.0, fy=2.0)
imgcontours = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #轉灰階
canny = cv2.Canny(img, 20, 400) #設定邊緣域值
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #找邊緣

for cnt in contours:
    cv2.drawContours(imgcontours, cnt, -1, (255, 0, 0), 4)

cv2.imshow('img_boki', img)
cv2.imshow('canny', canny)
cv2.imshow('imgcontours', imgcontours)

cv2.waitKey(0)