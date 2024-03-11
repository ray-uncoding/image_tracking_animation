import cv2

#img = cv2.imread('img_files/boki.jpg')  # 讀圖



img = cv2.imread('img_files/blue_triangle (3).png')  # 讀圖
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
imgcontours = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階
canny = cv2.Canny(img, 20, 400)  # 設定邊緣域值
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 找邊緣

for cnt in contours:
    cv2.drawContours(imgcontours, cnt, -1, (255, 0, 0), 4)  # 在複製的影像中畫出輪廓
    peri = cv2.arcLength(cnt, True)  # 計算閉合輪廓的邊長
    vertices = cv2.approxPolyDP(cnt, peri * 0.02, True) #計算近似的多邊形, 輸出頂點
    corners = len(vertices) #計算頂點數
    x, y, w, h = cv2.boundingRect(vertices) #把所有頂點位置以方形框選時的大小
    cv2.rectangle(imgcontours, (x,y), (x+w, y+h), (0, 255, 0), 4)

cv2.imshow('img_boki', img)
cv2.imshow('canny', canny)
cv2.imshow('imgcontours', imgcontours)

cv2.waitKey(0)


