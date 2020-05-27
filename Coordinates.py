import pyautogui
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Users\Antec\AppData\Local\Tesseract-OCR\tesseract.exe'
img  = Image.open("coordinates.png")

output = pytesseract.image_to_string(img)
output = output.split(',')

total = int(output[0]) + int(output[1])
print(output[0])
print(output[1])
print(total)
#print(output)
#print(len(output))
