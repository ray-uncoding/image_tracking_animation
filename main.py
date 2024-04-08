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
    camera_index = 0 
    video_path_01 = 'video_files/fried_riceball.mp4'
    threshold_area = 100 
    play_speed = 30

    found_blue = False
    found_blue_green = False
    found_red = False
    found_orange = False
    found_pink = False
    found_perple = False
    found_yellow = False
    found_green = False
    
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

        lower_blue = np.array([91, 59, 135])  # 91 118 59 172 135 255
        upper_blue = np.array([118, 172, 255])

        lower_blue_green = np.array([73, 44, 145])  # 73 129 44 165 145 224
        upper_blue_green = np.array([129, 165, 224])

        lower_red = np.array([0, 48, 181])  # 0 21 48 130 181 243
        upper_red = np.array([21, 130, 243])

        lower_orange = np.array([6, 89, 196])  # 6 24 89 189 196 247
        upper_orange = np.array([24, 189, 247])

        lower_pink = np.array([137, 43, 183])  # 137 178 43 103 183 251
        upper_pink = np.array([178, 103, 251])

        lower_perple = np.array([146, 39, 124])  # 146 179 39 118 124 194
        upper_perple = np.array([179, 118, 194])

        lower_yellow = np.array([11, 55, 160])  # 11 30 55 153 160 225
        upper_yellow = np.array([30, 153, 225])

        lower_green = np.array([30, 84, 150])  # 30 49 84 137 150 217
        upper_green = np.array([49, 137, 217])

        mask_blue       = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_blue_green = cv2.inRange(hsv, lower_blue_green, upper_blue_green)
        mask_red        = cv2.inRange(hsv, lower_red, upper_red)
        mask_orange     = cv2.inRange(hsv, lower_orange, upper_orange)
        mask_pink       = cv2.inRange(hsv, lower_pink, upper_pink)
        mask_perple     = cv2.inRange(hsv, lower_perple, upper_perple)
        mask_yellow     = cv2.inRange(hsv, lower_yellow, upper_yellow)
        mask_green      = cv2.inRange(hsv, lower_green, upper_green)

        contours_blue, _ = cv2.findContours(
            mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_blue_green, _ = cv2.findContours(
            mask_blue_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_red, _ = cv2.findContours(
            mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_orange, _ = cv2.findContours(
            mask_orange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_pink, _ = cv2.findContours(
            mask_pink, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_perple, _ = cv2.findContours(
            mask_perple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_yellow, _ = cv2.findContours(
            mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_green, _ = cv2.findContours(
            mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours_blue:
            area = cv2.contourArea(contour)
            if area > threshold_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                found_blue = True
            else:
                found_blue = False
        
        for contour in contours_blue_green:
            area = cv2.contourArea(contour)
            if area > threshold_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                found_blue_green = True
            else:
                found_blue_green = False
                
        for contour in contours_red:
            area = cv2.contourArea(contour)
            if area > threshold_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                found_red = True
            else:
                found_red = False       
                
        for contour in contours_orange:
            area = cv2.contourArea(contour)
            if area > threshold_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                found_orange = True
            else:
                found_orange = False        
                
        for contour in contours_pink:
            area = cv2.contourArea(contour)
            if area > threshold_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                found_pink = True
            else:
                found_pink = False        
                
        for contour in contours_perple:
            area = cv2.contourArea(contour)
            if area > threshold_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                found_perple = True
            else:
                found_perple = False
                
        for contour in contours_yellow:
            area = cv2.contourArea(contour)
            if area > threshold_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                found_yellow = True
            else:
                found_yellow = False        
        
        for contour in contours_green:
            area = cv2.contourArea(contour)
            if area > threshold_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                found_green = True
            else:
                found_green = False  
                
        #範例
        if found_blue :
            play_video(video_path_01, play_speed)

        found_blue = False
        found_blue_green = False
        found_red = False
        found_orange = False
        found_pink = False
        found_perple = False
        found_yellow = False
        found_green = False

        cv2.imshow('Processed Frame, press q to leave', frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    release_camera(cap)
    cv2.destroyAllWindows()

# 主程式
if __name__ == "__main__":
    main()
