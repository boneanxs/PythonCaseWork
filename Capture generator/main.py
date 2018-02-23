import string
import random
from PIL import Image,ImageFont,ImageDraw,ImageFilter

width = 240
height = 60

def random_char():
    return random.choice(string.ascii_letters)
def random_color_back():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def random_color_letter():
     return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
def generator(num):
    global width,height
    letters = ''
    img = Image.new('RGB',(width,height),(255,255,255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(r'arial.ttf',36)
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=random_color_back())
    for i in range(num):
        char = random_char()
        letters = letters + char
        draw.text((60 * i + 10,10),char,font=font,fill = random_color_letter())
    img = img.filter(ImageFilter.BLUR)
    return letters,img
if __name__ == '__main__':
    letters,result = generator(4)
    print(letters)
    result.save(r'E:/PythonCaseWork/Capture generator/capture.jpeg','jpeg')