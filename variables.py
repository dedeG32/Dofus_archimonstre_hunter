##############################main#########################################
import csv
import time
import cv2
from pygame import mixer

# ___________________________________VARIABLES_____________________________________
#      image
archimonstre_img = cv2.imread("archimonstrepic.jpg", cv2.IMREAD_COLOR)  # Path to the template image you want to find
#template = cv2.imread(image_to_find, cv2.IMREAD_COLOR)  # Load the template image in BGR format

#       Alarm
mixer.init()
trouve_alert = mixer.Sound('weeb-alert-182941.mp3')  # Path to the sound file to play when the image is found
fin_de_exploration = mixer.Sound('archiprogram_end.mp3')

#       click
width, height = 1920, 1080  # largeur , et hauteur de l'ecran

data = dict()
with open("mouse_clicks.csv", mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')  # Assuming comma is the delimiter
    for row in reader:
        if len(row) == 2:  # Ensure row has exactly 2 elements
            key, positions = row
            try:
                # Use ast.literal_eval for safe evaluation
                data[key] = eval(positions)
            except (SyntaxError, ValueError):
                print(f"Skipping malformed entry: {row}")

def get_int(min, max) -> int:
    while True:
       try:
            chose = int(input("Enter: "))
            if min <= chose <= max:
                return chose
            else:
                print(f"please input a number between {min} and {max}")
       except :
            print("Please enter a valid integer")


def menu(zone):
    print("select the mode:")
    print("0. Continuer l'exploration")
    print("1. archimonstres finder")
    print("2. farm")
    print("3. detecteur")
    print("4. record movement")
    chose = get_int(0,4)
    from mouvement import mouvement

    match chose:
        case 0:
            with open("resume.txt", "r") as file:
                resume = file.read()
            #print(eval(resume))
            mouvement(eval(resume))

        case 1:
             mouvement(data[zone], archimonstre_img)

        case 2:
            print("Told you! Nothing here.")
            menu()

        case 3:
            from detecteur import find_image_on_screen
            while not find_image_on_screen(archimonstre_img):
                print("r")
                time.sleep(3)
            #trouve_alert.play()
            #time.sleep(15)
        case 4:
            import moucerecordgui
            root = moucerecordgui.tk.Tk()
            app = moucerecordgui.MouseRecorderApp(root)
            root.mainloop()



with open("resume.txt", "r") as file:
        resume = file
print(resume)