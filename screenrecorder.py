# importing the required packages
import pyautogui
import cv2
import numpy as np
import datetime
import time

# Specify resolution
resolution = pyautogui.size()

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = f"C:/Users/Dos/Desktop/Recording_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"

# Specify frames rate. We can choose any
# value and experiment with it
fps = 30.0

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)
prev_time = time.time()

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    current_time = time.time()
    fps_display = 1 / (current_time - prev_time)
    prev_time = current_time

    cv2.putText(frame, f"FPS: {int(fps_display)}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2)

    # Write it to the output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)

    # Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
