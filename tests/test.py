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
    if("|" in text):
        text = text.replace("|","I")

    # 3 Second delay, begins typing
    time.sleep(3)
    keyboard.write(text)

"""Main Function"""
if __name__ == "__main__":
    writer() #Calls writer function
