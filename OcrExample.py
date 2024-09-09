#opencv 
import cv2
import pytesseract

#point out where the tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\TiagoAlmeida\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('comanda.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening

data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print(data)