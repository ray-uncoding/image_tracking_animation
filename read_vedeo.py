import cv2
#cap = cv2.VideoCapture('vedeo_files/boki.mp4')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    if ret:
        cv2.imshow('video press q to leave', frame)
    else:
        break
    if cv2.waitKey(20) == ord('q'):
        break
    
