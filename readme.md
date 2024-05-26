# 顏色偵測影片播放器專案

## 作者
潘林陞 (ray-uncoding)

## 專案描述
這個專案利用 OpenCV 來偵測攝影機中的顏色範圍，根據偵測到的顏色組合來播放相應的影片。專案支援全螢幕播放影片，並能夠根據任意按鍵停止播放。

## 環境設置

### 安裝需求
1. Python 3.x
2. OpenCV
3. NumPy

你可以使用以下命令來安裝所需的 Python 庫：

```bash
pip install opencv-python numpy

.
├── main.py
├── video_files
│   ├── video_A.mp4
│   ├── video_B.mp4
│   ├── ...
└── README.md
