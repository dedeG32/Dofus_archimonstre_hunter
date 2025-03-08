# import csv
# data = dict()
# with open("mouse_clicks.csv", mode='r', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=';')  # Assuming comma is the delimiter
#     for row in reader:
#         if len(row) == 2:  # Ensure row has exactly 2 elements
#             key, positions = row
#             try:
#                 # Use ast.literal_eval for safe evaluation
#                 data[key] = eval(positions)
#             except (SyntaxError, ValueError):
#                 print(f"Skipping malformed entry: {row}")
#
#
# "modifier la variable zone"
# zone = None
# ############################################
# while True:
#     for i in data[zone]:
#         time.sleep(10)
#         pyautogui.click(i)
#

def farm():
    pass
