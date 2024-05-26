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

以下是資料夾結構:
.
├── main.py
├── video_files
│   ├── video_A.mp4
│   ├── video_B.mp4
│   ├── ...
└── README.md


注意事項：
1. 下載python時, 記得去檢視進階系統設定去全域變數把使用者設定跟系統設定的path新增出python exe的路徑跟script的路徑, 像以下這樣
    C:\Users\ray62\AppData\Local\Programs\Python\Python312
    C:\Users\ray62\AppData\Local\Programs\Python\Python312\Scripts
2. 開啟vscode後第一件事情，下載這個
    pip install opencv-python
3.
