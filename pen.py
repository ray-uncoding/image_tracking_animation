import cv2
import numpy as np

#min , max
pencolorHSV = [[10, 164, 121, 27, 231, 185]]
pointcolor = [[255, 0, 0]]
drawpoint = []  #x, y, id

cap = cv2.VideoCapture(1)

def find_pen(img):
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i in range(len(pencolorHSV)):
        lower = np.array(pencolorHSV[i][:3])
        upper = np.array(pencolorHSV[i][3:6])

        mask = cv2.inRange(HSV, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        
        penx, peny = find_Contour(mask)
        if peny != -1:
            drawpoint.append([penx, peny, i])
        
        cv2.circle(imgcontours, (penx, peny), 10, pointcolor[i], cv2.FILLED)
        #cv2.imshow('result', result)
        #cv2.imshow('contours', imgcontours)

def find_Contour(img):
    x, y, w, h = -1, -1, -1, -1
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 找邊緣
    for cnt in contours:
        cv2.drawContours(imgcontours, cnt, -1, (255, 0, 0), 4)  # 在複製的影像中畫出輪廓
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)  # 計算閉合輪廓的邊長
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True) #計算近似的多邊形, 輸出頂點
            corners = len(vertices) #計算頂點數
            x, y, w, h = cv2.boundingRect(vertices) #把所有頂點位置以方形框選時的大小
            cv2.rectangle(imgcontours, (x,y), (x+w, y+h), (0, 255, 0), 4)
    
    return x + w//2, y
        
def draw(drawpoint):
    for point in drawpoint:
        cv2.circle(imgcontours, (point[0], point[1]), 10, pointcolor[point[2]], cv2.FILLED)

# 主程式, 不斷刷新並更新畫面
while True:

    # 抓取鏡頭參數, 參數1. 是否於啟動中, 參數2. 畫面源
    ret, frame = cap.read()
    keyName = cv2.waitKey(10)                # 抓取指令, 等50毫秒
    #frame = cv2.resize(frame, (1600, 900))    # 縮小尺寸加快速度
    
    if not ret:
        print("鏡頭中斷, 重啟程式或重接鏡頭")
        break
    else:
        #imgcontours = frame.copy()
        imgcontours = cv2.imread('img_files/boki.jpg')
        
        find_pen(frame)
        draw(drawpoint)
        cv2.imshow('studio', frame)
        cv2.imshow('contours', imgcontours)
   
    # 指令 q , 關閉程式
    if keyName == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()