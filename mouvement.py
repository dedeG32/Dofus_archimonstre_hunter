import time
import pyautogui
from detecteur import find_image_on_screen
from variables import trouve_alert, fin_de_exploration
def mouvement(zone, img=None):
    time.sleep(5)
    x = 0
    for index, i in enumerate(zone):
        if find_image_on_screen(img):
            #trouve_alert.play()
            print("Target image successfully detected! Sound played.")
            resume(index, zone)
            time.sleep(14)
            break
        pyautogui.click(i)
        x += 1
        print(x)
        time.sleep(7)


        print("Target image not found. Clicked on the specified location instead.")

    fin_de_exploration.play()
    time.sleep(10)

def resume(index, zone):
    with open('resume.txt', mode='w', encoding='utf8') as file:
        file.write(str(zone[index:]))




if __name__ == "__main__":
    import cv2
    archimonstre_img = cv2.imread("archimonstrepic.jpg", cv2.IMREAD_COLOR)  # Path to the template image you want to find
    mouvement("dragon1", archimonstre_img)


