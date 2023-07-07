import PIL
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance
import cv2 as cv
import pytesseract

image = Image.open("Test.png")
image = image.convert('RGB')

font = ImageFont.truetype("c:/Windows/Fonts/Arial.ttf", 50)

new_image = Image.new(image.mode, (image.width, image.height+70))
new_image.paste(image, (0,0))

images = []
intensities = (0.1, 0.5, 0.9)
channels = [0,1,2]

for chan in channels:
    for inte in intensities:
        new = new_image.copy()
        text = f"channel {chan} intensity {inte}"
        ImageDraw.Draw(new).text((0,new_image.height-70), text, font = font)
        r,g,b = new.split()
        if  chan == 0:
            r = r.point(lambda x: x*inte)
        elif chan == 1:
            g = g.point(lambda x: x*inte)
        else:
            b = b.point(lambda x: x*inte)
        print(type(r))
        last = Image.merge('RGB', (r,g,b))
        images.append(last)

contact_sheet = PIL.Image.new(new_image.mode, (new_image.width * 3, new_image.height * 3))
x = 0
y = 0
for img in images:
    contact_sheet.paste(img, (x,y))
    x += img.width
    if x == contact_sheet.width:
        x = 0
        y += img.height

contact_sheet = contact_sheet.resize((int(contact_sheet.width/2), int(contact_sheet.height/2)))
contact_sheet.show()
#
#=======================================================================================================================


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = Image.open("Untitled 2.png")

image2 = image.crop((310,150,700,260)).resize((image.width*10, image.height*10)).convert('L')

def bina(image, thresh):
    for x in range(image.width):
        for y in range(image.height):
            if image.getpixel((x,y)) < thresh:
                image.putpixel((x, y), 0)
            else:
                image.putpixel((x, y),255)
    return image
bina(image2, 155).show()
print(pytesseract.image_to_string(bina(image2, 154)).lower())

text = pytesseract.image_to_string(image2)
print(text)

#=======================================================================================================================

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier('C:/Users/Psionic/AppData/Local/Programs/Python/Python38/Lib/site-packages/cv2/'
                                   'data/haarcascade_eye.xml')

image = cv.imread('Test.png')
faces = face_cascade.detectMultiScale(image)


def show_rect(faces):
    image = Image.open('Test.png').convert('RGB')
    for x,y,width,height in faces:
        ImageDraw.Draw(image).rectangle((x, y, x+width, y+height), outline='white')
    image.show()

cv_img_bin=cv.threshold(image,120,255,cv.THRESH_BINARY)[1]
faces = face_cascade.detectMultiScale(image, 1.25)
show_rect(faces)
