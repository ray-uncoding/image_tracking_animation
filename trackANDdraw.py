import cv2

# 全域變數宣告
multiTracker = cv2.legacy.MultiTracker_create()  # 建立多物件追蹤器
tracking = False                                 # 設定追蹤尚未開始
colors = [(0, 0, 255),
          (0, 255, 255),
          (255, 255, 255),
          (100, 255, 255),
          (50, 255, 255)]                        # 建立外框色彩清單

# 如果鏡頭未初始化，顯示不能開啟鏡頭
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("鏡頭中斷, 重啟程式或重接鏡頭")
    exit()

# 主程式, 不斷刷新並更新畫面
while True:

    # 抓取鏡頭參數, 參數1. 是否於啟動中, 參數2. 畫面源
    ret, frame = cap.read()
    if not ret:
        print("鏡頭中斷, 重啟程式或重接鏡頭")
        break
    #frame = cv2.resize(frame, (800, 450))    # 縮小尺寸加快速度
    frameCopy = frame.copy()                 # 複製一份
    keyName = cv2.waitKey(50)                # 抓取指令, 等50毫秒

    # 指令 q , 關閉程式
    if keyName == ord('q'):
        break

    # 指令 a , 手動標記
    if keyName == ord('a'):
        # 標記外框後設定該物件的追蹤演算法
        for i in range(5):            
            area = cv2.selectROI('select object',
                                 frame,
                                 showCrosshair=False,
                                 fromCenter=False)
            tracker = cv2.legacy.TrackerCSRT_create()
            multiTracker.add(tracker, frame, area)  # 將該物件加入 multiTracker
        tracking = True  # 設定 True 開始追蹤

    if tracking:
        # 更新 multiTracker, 如果成功抓取, 就取二點畫方框
        success, points = multiTracker.update(frame)  
        a = 0
        if success:
            for i in points:
                p1 = (int(i[0]), int(i[1]))
                p2 = (int(i[0] + i[2]), int(i[1] + i[3]))
                cv2.rectangle(frame, p1, p2, colors[a], 3)
                a = a + 1
                
    cv2.imshow('studio', frame)


cap.release()
cv2.destroyAllWindows()
