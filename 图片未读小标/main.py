from PIL import Image,ImageFont,ImageDraw

im = Image.open('E:/PythonCaseWork/图片未读小标/raw.jpg')
w,h = im.size
w = 5 * w / 6
h = 1 * h / 6
font = ImageFont.truetype(r'arial.ttf',30)
draw = ImageDraw.Draw(im)
draw.text((w,h),text='12',font=font,fill=(0,85,85,0))
im.save('E:/PythonCaseWork/图片未读小标/modified.jpg')
print('succeed!')
