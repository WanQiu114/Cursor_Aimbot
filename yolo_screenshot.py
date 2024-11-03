import cv2
import numpy as np
import pyautogui
import time
import os

# set up your saving folder
save_dir = "game_screenshots"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# set up the area where you want to do screenshot, at this point I will do default 1920 * 1080
region = (0, 0, 1920, 1080)  


interval = 2  # screenshot every 2 sec
total_images = 70  # take 70 in total, but better to set more

def capture_screen(region=None):
    """
    use opencv to capture the screen
    """
    screenshot = pyautogui.screenshot(region=region)
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)
    return frame

def main():
    count = 0
    while count < total_images:
        
        frame = capture_screen(region=region)
        save_path = os.path.join(save_dir, f"screenshot_{count + 1}.jpg")
        cv2.imwrite(save_path, frame)
        print(f"Saved screenshot {count + 1} to {save_path}")

        count += 1
        time.sleep(interval)

if __name__ == "__main__":
    main()