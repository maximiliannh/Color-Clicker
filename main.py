import pyautogui
import time
from PIL import ImageGrab

target_color = (0, 0, 0)  # RGB
area_coordinates = (x1, y1, x2, y2) #your pixel coordinates here

while True:
    screenshot = ImageGrab.grab(bbox=area_coordinates)
    pixels = screenshot.load()

    color_found = False
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            pixel_color = pixels[x, y]
            if pixel_color == target_color:
                color_found = True
                break
        if color_found:
            break

    if color_found:
        pyautogui.click()

    time.sleep(0.5) 
