import cv2
import numpy as np

def play_video(file_name, speed):
    cap = cv2.VideoCapture(file_name)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Video Player', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (width, height))

        cv2.imshow('Video Player', frame)
        if cv2.waitKey(int(1000 / speed)) & 0xFF != 0xFF:
            break

    cap.release()
    cv2.destroyAllWindows()

def initialize_camera(camera_index):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Error: Unable to open the camera {camera_index}.")
        return None
    return cap

def release_camera(cap):
    if cap is not None:
        cap.release()

def apply_mask(frame, mask):
    return cv2.bitwise_and(frame, frame, mask=mask)

def process_contours(contours, threshold_area, frame):
    for contour in contours:
        if cv2.contourArea(contour) > threshold_area:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            return True
    return False

def load_and_resize_mask(mask_path, frame_shape):
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    if mask is None:
        print(f"Error: Unable to load the mask image from {mask_path}.")
        return None
    return cv2.resize(mask, (frame_shape[1], frame_shape[0]))

def main():
    camera_indices = [1, 2]  # 使用的攝像頭索引
    mask_paths = ['img_files/mask1.png', 'img_files/mask2.png']  # 對應的遮罩文件路徑
    threshold_area = 500  # 最小區域閾值設定
    play_speed = 30

    video_map = {
        'A': 'video_files/video_A.mp4',
        'B': 'video_files/video_B.mp4',
        'C': 'video_files/video_C.mp4',
        'D': 'video_files/video_D.mp4',
        'E': 'video_files/video_E.mp4',
        'F': 'video_files/video_F.mp4',
        'G': 'video_files/video_G.mp4',
        'H': 'video_files/video_H.mp4',
        'AB': 'video_files/video_AB.mp4',
        'AC': 'video_files/video_AC.mp4',
        'AD': 'video_files/video_AD.mp4',
        'AE': 'video_files/video_AE.mp4',
        'AF': 'video_files/video_AF.mp4',
        'AG': 'video_files/video_AG.mp4',
        'AH': 'video_files/video_AH.mp4',
        'BC': 'video_files/video_BC.mp4',
        'BD': 'video_files/video_BD.mp4',
        'BE': 'video_files/video_BE.mp4',
        'BF': 'video_files/video_BF.mp4',
        'BG': 'video_files/video_BG.mp4',
        'BH': 'video_files/video_BH.mp4',
        'CD': 'video_files/video_CD.mp4',
        'CE': 'video_files/video_CE.mp4',
        'CF': 'video_files/video_CF.mp4',
        'CG': 'video_files/video_CG.mp4',
        'CH': 'video_files/video_CH.mp4',
        'DE': 'video_files/video_DE.mp4',
        'DF': 'video_files/video_DF.mp4',
        'DG': 'video_files/video_DG.mp4',
        'DH': 'video_files/video_DH.mp4',
        'EF': 'video_files/video_EF.mp4',
        'EG': 'video_files/video_EG.mp4',
        'EH': 'video_files/video_EH.mp4',
        'FG': 'video_files/video_FG.mp4',
        'FH': 'video_files/video_FH.mp4',
        'GH': 'video_files/video_GH.mp4',
        'ABC': 'video_files/video_ABC.mp4',
        'ABD': 'video_files/video_ABD.mp4',
        'ABE': 'video_files/video_ABE.mp4',
        'ABF': 'video_files/video_ABF.mp4',
        'ABG': 'video_files/video_ABG.mp4',
        'ABH': 'video_files/video_ABH.mp4',
        'ACD': 'video_files/video_ACD.mp4',
        'ACE': 'video_files/video_ACE.mp4',
        'ACF': 'video_files/video_ACF.mp4',
        'AFG': 'video_files/video_AFG.mp4',
        'AFH': 'video_files/video_AFH.mp4',
        'AGH': 'video_files/video_AGH.mp4',
        'BCD': 'video_files/video_BCD.mp4',
        'BCE': 'video_files/video_BCE.mp4',
        'BCF': 'video_files/video_BCF.mp4',
        'BCG': 'video_files/video_BCG.mp4',
        'BCH': 'video_files/video_BCH.mp4',
        'BDE': 'video_files/video_BDE.mp4',
        'BDF': 'video_files/video_BDF.mp4',
        'BDG': 'video_files/video_BDG.mp4',
        'BDH': 'video_files/video_BDH.mp4',
        'BEF': 'video_files/video_BEF.mp4',
        'BEG': 'video_files/video_BEG.mp4',
        'BEH': 'video_files/video_BEH.mp4',
        'BFG': 'video_files/video_BFG.mp4',
        'BFH': 'video_files/video_BFH.mp4',
        'BGH': 'video_files/video_BGH.mp4',
        'CDE': 'video_files/video_CDE.mp4',
        'CDF': 'video_files/video_CDF.mp4',
        'CDG': 'video_files/video_CDG.mp4',
        'CDH': 'video_files/video_CDH.mp4',
        'CEF': 'video_files/video_CEF.mp4',
        'CEG': 'video_files/video_CEG.mp4',
        'CEH': 'video_files/video_CEH.mp4',
        'CFG': 'video_files/video_CFG.mp4',
        'CFH': 'video_files/video_CFH.mp4',
        'CGH': 'video_files/video_CGH.mp4',
        'DEF': 'video_files/video_DEF.mp4',
        'DEG': 'video_files/video_DEG.mp4',
        'DEH': 'video_files/video_DEH.mp4',
        'DFG': 'video_files/video_DFG.mp4',
        'DFH': 'video_files/video_DFH.mp4',
        'DGH': 'video_files/video_DGH.mp4',
        'EFG': 'video_files/video_EFG.mp4',
        'EFH': 'video_files/video_EFH.mp4',
        'EGH': 'video_files/video_EGH.mp4',
        'FGH': 'video_files/video_FGH.mp4'
    }

    color_ranges = {
        'A': ([18, 80, 155], [38, 194, 255]),  # Yellow
        'B': ([105, 18, 53], [155, 80, 158]),  # Purple
        'C': ([3, 109, 109], [7, 211, 255]),  # Red
        'D': ([0, 50, 137], [6, 119, 255]),  # Pink
        'E': ([60, 40, 57], [93, 220, 249]),  # Cyan
        'F': ([91, 54, 110], [132, 255, 200]),  # Light Blue
        'G': ([8, 122, 154], [18, 200, 255]),  # Orange
        'H': ([37, 62, 70], [55, 131, 220])   # Green
    }

    caps = [initialize_camera(index) for index in camera_indices]
    if any(cap is None for cap in caps):
        return

    masks = [load_and_resize_mask(path, (int(caps[0].get(cv2.CAP_PROP_FRAME_HEIGHT)), int(caps[0].get(cv2.CAP_PROP_FRAME_WIDTH)))) for path in mask_paths]
    if any(mask is None for mask in masks):
        for cap in caps:
            release_camera(cap)
        return

    while True:
        frames = []
        for cap, mask in zip(caps, masks):
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read a frame from the camera.")
                return
            masked_frame = apply_mask(frame, mask)
            frames.append(masked_frame)

        # 合併兩個鏡頭的畫面
        combined_frame = np.hstack(frames)
        
        # 應用高斯模糊來減少雜訊
        blurred = cv2.GaussianBlur(combined_frame, (11, 11), 0)
        
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        colors_detected = []

        for color, (lower, upper) in color_ranges.items():
            color_mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
            contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            detected = process_contours(contours, threshold_area, combined_frame)
            colors_detected.append(detected)
        
        # 決定要播放哪個影片
        detected_colors = [color for color, detected in zip(color_ranges.keys(), colors_detected) if detected]
        video_key = ''.join(detected_colors)

        if video_key in video_map:
            play_video(video_map[video_key], play_speed)

        # 顯示應用遮罩後的影像
        cv2.imshow('Masked Frame', combined_frame)
        cv2.imshow('Processed Frame, press q to leave', combined_frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    for cap in caps:
        release_camera(cap)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
