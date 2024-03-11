import cv2
import numpy as np
from read_vedeo import play_video

def initialize_camera(camera_index):
    # 開啟攝像頭
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print("Error: Unable to open the camera.")
        return None

    return cap

def release_camera(cap):
    # 釋放攝像頭
    if cap is not None:
        cap.release()

def main():
    camera_index = 0  # 調整這個數值以匹配你的攝像頭
    video_path = 'vedeo_files/fried_riceball.mp4'
    threshold_area = 500  # 調整此數值以控制橘色長方形的面積閾值
    play_speed = 30  # 調整此數值以控制撥放速度，數值越小速度越快

    found_orange = None  # 追蹤是否找到符合條件的橘色長方形

    # 初始化攝像頭
    cap = initialize_camera(camera_index)
    if cap is None:
        return

    while True:
        # 讀取一帧影像
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to read a frame from the camera.")
            break

        # 將影像轉換成HSV色彩空間
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 定義橘色的HSV範圍
        lower_orange = np.array([5, 100, 100])
        upper_orange = np.array([15, 255, 255])

        # 透過色彩過濾找到橘色區域
        mask = cv2.inRange(hsv, lower_orange, upper_orange)

        # 找到橘色區域的輪廓
        contours, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 遍歷輪廓，尋找橘色長方形
        for contour in contours:
            # 計算輪廓的面積
            area = cv2.contourArea(contour)

            # 如果面積大於閾值，框選起來
            if area > threshold_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                found_orange = True
            else:
                found_orange = False

        # 如果找到符合條件的橘色長方形，則撥放影片
        if found_orange:
            play_video(video_path, play_speed)
            found_orange = False  # 重置 found_orange，以便下一次迴圈重新檢測

        # 顯示處理後的畫面
        cv2.imshow('Processed Frame', frame)

        # 按下 'q' 鍵離開迴圈
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    # 釋放攝像頭並關閉視窗
    release_camera(cap)
    cv2.destroyAllWindows()

# 主程式
if __name__ == "__main__":
    main()
