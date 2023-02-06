from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = '/opt/homebrew/Cellar/tesseract/5.2.0/bin/tesseract'
path_to_image = 'data/sampleText1.png'

pytesseract.tesseract_cmd = path_to_tesseract

img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)

print()
print(text)