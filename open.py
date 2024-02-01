import cv2
import datetime
import os

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error:Could not open camera.")
    exit()


save_directory="D:\camera laptop"
os.makedirs(save_directory, exist_ok=True)
frame_count=0

while True:
    ret, frame=cap.read()
    cv2.imshow('Live stream',frame)

    key=cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        timestamp=datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        image_name=f"{save_directory}/captured_image_{timestamp}.png"
        cv2.imwrite(image_name, frame)
        print(f"Image saved as {image_name}")
        frame_count+=1

    elif key == ord('q'):
        break   

cap.release()     