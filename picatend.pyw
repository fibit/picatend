import sys
import cv2
from tkinter import messagebox
from datetime import datetime

TITLE = "Picatend"

def initialize_camera():
    for port in range(1, -1, -1):
        camera = cv2.VideoCapture(port, cv2.CAP_ANY)
        if camera.isOpened():
            return camera
    messagebox.showerror("Error", "Camera not found!")
    sys.exit(1)

def capture_and_display(camera):
    while True:
        connected, frame = camera.read()
        if not connected:
            messagebox.showerror("Error", "Camera lost connection!")
            break

        cv2.imshow(TITLE, frame)

        key = cv2.waitKey(1) & 0xFF
        if key == 27 or cv2.getWindowProperty(TITLE, cv2.WND_PROP_VISIBLE) < 1:
            save_frame(frame)
            break

def save_frame(frame):
    now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"{now}.jpg"
    cv2.imwrite(filename, frame)

def main():
    camera = initialize_camera()
    capture_and_display(camera)
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
