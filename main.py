from PIL import Image, ImageFilter

img = Image.open("./astro.jpg")
img.thumbnail((400, 400))
print(img.size)
img = img.save('./astro_small.jpg')

