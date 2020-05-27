import pyautogui
from PIL import Image
from pytesseract import *
#Note: You have to change the path below to your tesseract.exe location
pytesseract.tesseract_cmd = r'C:\Users\Antec\AppData\Local\Tesseract-OCR\tesseract.exe'

#This line stores the image texttoconvert.png inside the img variable
img  = Image.open("texttoconvert.png")

#Note: You can use pyautogui to fetch the screenshot instead of fetching it from a file
#img = pyautogui.screenshot(region=(10,10,10,10))

#This line uses pytesseract's image_to_string function to convert the image stored in the variable (img) into a string (text) that will be stored in the (output variable)
output = pytesseract.image_to_string(img)

#We can now print out the output
print(output)

#output = output.split(',')
#print(output[0])
#print(output[1])
#print(output)
#print(len(output))
