# Resizing the image usign the Pillow Library

from PIL import Image
img = Image.open('test.jpg')
print(f"Current size : {img.size}")

resized_img = img.resize((500, 250))
print('Resized is ', resized_img.size)

resized_img.save('resized Image.jpg')