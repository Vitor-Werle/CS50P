import sys
from PIL import Image, ImageOps

muppet = Image.open("before1.jpg")
shirt = Image.open("shirt.png")

size = shirt.size

muppet = ImageOps.fit(muppet, size)

muppet.paste(shirt, shirt)

muppet.save("pront.png")