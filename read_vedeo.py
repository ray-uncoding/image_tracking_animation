# 影片播放器程式碼
# 作者：[潘林陞 ray-uncoding]
# 描述：這個程式使用OpenCV播放影片，支援全螢幕顯示和任意按鍵離開。
# 使用方法：將欲撥放的影片檔案名稱和撥放速度作為參數傳入play_video函數。

import cv2

def play_video(file_name, speed):
    """
    影片播放函數

    參數：
    - file_name: 字串，欲撥放的影片檔案名稱（包含路徑）
    - speed: 數值，撥放速度，數值越小速度越快

    使用範例：
    file_name = 'vedeo_files/fried_riceball.mp4'
    play_speed = 30  # 調整此數值以控制撥放速度，數值越小速度越快
    play_video(file_name, play_speed)
    """
    cap = cv2.VideoCapture(file_name)

    # 獲取影片的寬度和高度
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 建立一個可調整大小的窗口
    cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Video Player', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 將影片調整為全螢幕大小
        frame = cv2.resize(frame, (width, height))

        cv2.imshow('Video Player', frame)

        # 等待任意按鍵觸發，如果按下任意按鍵則離開
        if cv2.waitKey(int(1000 / speed)) & 0xFF != 0xFF:
            break

    cap.release()
    cv2.destroyAllWindows()

# 使用範例
file_name = 'vedeo_files/fried_riceball.mp4'
play_speed = 30  # 調整此數值以控制撥放速度，數值越小速度越快
play_video(file_name, play_speed)
