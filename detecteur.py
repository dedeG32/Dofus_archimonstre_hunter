import numpy as np
import pyautogui
import cv2
import logging
from variables import  archimonstre_img, trouve_alert
import time
def find_image_on_screen(template=None, threshold=0.8):
    try:
        if template == None: return False
    except:
        pass
    try:
        # Take a screenshot of the entire screen
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a numpy array (BGR format for OpenCV)
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # Perform template matching
        result = cv2.matchTemplate(screenshot_bgr, template, cv2.TM_CCOEFF_NORMED)

        # Find the location of the best match, and get its value and location
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Check if the best match is above the threshold
        if max_val >= threshold:
            trouve_alert.play()
            time.sleep(15)
            return True
        else: return False
        #return max_val >= threshold

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    while True:
        find_image_on_screen(archimonstre_img)
    # from pygame import mixer
    # import cv2
    # import time
    #
    # archimonstre= cv2.imread("archimonstrepic.jpg", cv2.IMREAD_COLOR)
    # mixer.init()
    # trouve_alert = mixer.Sound('weeb-alert-182941.mp3')
    # while True:
    #     time.sleep(5)
    #     if find_image_on_screen(archimonstre):
    #         trouve_alert.play()
    #         time.sleep(15)