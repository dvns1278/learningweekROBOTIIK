import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Kamera tidak terdeteksi")
    exit()

cv2.namedWindow('Camera Filters')

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Tidak bisa membaca frame")
        break

    frame = cv2.flip(frame, 1)

    resized_frame = cv2.resize(frame, (320, 240))  

    grid1 = resized_frame.copy()

    grid2 = resized_frame.copy()
    pink_overlay = np.full_like(grid2, [255, 182, 193])  
    grid2 = cv2.addWeighted(grid2, 0.5, pink_overlay, 0.5, 0)  

    grid3 = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    grid3 = cv2.cvtColor(grid3, cv2.COLOR_GRAY2BGR)

    hsv = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    grid4 = cv2.bitwise_and(resized_frame, resized_frame, mask=mask)

    if cv2.countNonZero(mask) == 0:
        grid4 = resized_frame.copy()

    top_row = np.hstack((grid1, grid2))
    bottom_row = np.hstack((grid3, grid4))
    final_frame = np.vstack((top_row, bottom_row))

    cv2.imshow('Camera Filters', final_frame)

    if cv2.waitKey(1) & 0xFF == 13:  
        timestamp = cv2.getTickCount()
        filename = f"captured_image_{timestamp}.png"
        cv2.imwrite(filename, final_frame)
        print(f"Image saved as {filename}")
    
    if cv2.waitKey(1) & 0xFF == ord(' ') or cv2.getWindowProperty('Camera Filters', cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()