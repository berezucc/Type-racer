import keyboard
import time
import pyautogui

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'T:\Tesseract\tesseract.exe'
#https://towardsdatascience.com/read-text-from-image-with-one-line-of-python-code-c22ede074cac <-- Convert image to text docs

"""Screenshot Function --> Takes a Screenshot Of Textbox"""
def screenShot():
    #Gets coordinates of "change display format button"
    coords = pyautogui.locateOnScreen("lights.JPG", confidence = 0.9)

    #Gets center of those coordinates
    coordsCenter = pyautogui.center(coords)

    #Calculations to get rough perimeter of text box with prompt
    x1 = int(coords[0])-370
    y1 = int(coords[1])+70
    coordsfix = (x1,y1,800,140)
    #Sets new coordinates, screenshots, and saves image
    im = pyautogui.screenshot(region=coordsfix)
    im.save(r"C:\Users\nikit\Desktop\Repositories\Type-racer\screen.png")

"""Image Function --> Reads Text From Image"""
def imageReader():
    screenShot()
    #img = cv2.imread('text.JPG') #Reads image file
    img = cv2.imread('screen.png') #Reads image file
    text = pytesseract.image_to_string(img) #Extracts text from imageFile

    return text #Returns text

"""Writer Function --> Types Keys"""
def writer():
    text = imageReader() #Saves text to write

    # Cleans text and fixes any bugs
    text = text.split("change display format")
    text = text[0].replace("change display format","")
    if(text[0] == "["):
        text = text[1:]
    if("|" in text or "1" in text):
        text = text.replace("|","I")
        text = text.replace("1","I")

    # 3 Second delay, begins typing
    time.sleep(4)
    #keyboard.write(text)
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.05)

"""Main Function"""
if __name__ == "__main__":
    writer() #Calls writer function
"""

"""