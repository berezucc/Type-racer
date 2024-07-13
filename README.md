# Type Racer Script
This script automates typing on the Type Racer website by capturing a screenshot of the textbox, converting the image to text using OCR (Optical Character Recognition), and then typing out the extracted text. The implementation uses `pyautogui`, `pytesseract`, and `opencv2`.

## Features
- Captures a screenshot of the textbox on the Type Racer website.
- Extracts text from the screenshot using Tesseract OCR.
- Automatically types the extracted text in the textbox.
## Requirements
- Python 3.x
- `pyautogui`
- `pytesseract`
- `opencv-python`
- Tesseract OCR installed and configured

## Installation
1. Clone the Repository:

```sh
git clone https://github.com/yourusername/type-racer-script.git
cd type-racer-script
```
2. Install the Required Python Packages:

```sh
pip install pyautogui pytesseract opencv-python keyboard
```
3. Install Tesseract OCR:

Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).

Configure the tesseract_cmd path in the script:

```python
pytesseract.pytesseract.tesseract_cmd = r'T:\Tesseract\tesseract.exe'
```
4. Place the Image File:

Ensure you have an image file named lights.JPG in the same directory as the script. This image is used to locate the textbox on the screen.

## Usage
1. Start the Type Racer Game:

Open your browser and navigate to the Type Racer website. Start a new game.

2. Run the Script:

Execute the script:

```sh
python typeracer.py
```
The script will locate the textbox, capture a screenshot, extract the text, and automatically type it into the textbox.

### Script Details
#### Screenshot Function
Captures a screenshot of the textbox area.

```python
def screenShot():
    coords = pyautogui.locateOnScreen("lights.JPG", confidence=0.9)
    coordsCenter = pyautogui.center(coords)
    x1 = int(coords[0])-370
    y1 = int(coords[1])+70
    coordsfix = (x1, y1, 800, 140)
    im = pyautogui.screenshot(region=coordsfix)
    im.save(r"C:\Users\nikit\Desktop\Repositories\Type-racer\screen.png")
```
#### Image Reader Function
Extracts text from the screenshot using Tesseract OCR.

```python
def imageReader():
    screenShot()
    img = cv2.imread('screen.png')
    text = str(pytesseract.image_to_string(img, lang="eng"))
    return text
```
#### Writer Function
Types the extracted text into the textbox.

```python
def writer():
    text = imageReader()
    text = text.split("change display format")
    text = text[0].replace("change display format", "")
    text = ' '.join(text.splitlines())
    if(text[0] == "["):
        text = text[1:]
    if("|" in text or "1" in text or "\\" in text or "!" in text):
        text = text.replace("|", "I")
        text = text.replace("1", "I")
        text = text.replace("\\", "I")
        text = text.replace("!", "I")
    print(text)
    time.sleep(3)
    for char in text:
        keyboard.write(char)
        time.sleep(0.01)
```
#### Main Function
Runs the writer function to start the process.

```python
if __name__ == "__main__":
    writer()
```
## Notes
Adjust the coordinates in the screenShot function if the textbox location changes.
Ensure Tesseract OCR is correctly installed and configured.
## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
