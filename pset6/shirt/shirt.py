import sys
from PIL import Image, ImageOps
import os

if len(sys.argv) < 3 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")
else:
    base1, ext1 =  os.path.splitext(sys.argv[1])
    base2, ext2 = os.path.splitext(sys.argv[2])
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
    try:
        #OPEN 2 IMAGES
        shirt = Image.open("shirt.png")
        before = Image.open(sys.argv[1])
        #Get size
        size = shirt.size
        #crop and resize the input
        before = ImageOps.fit(before, size)
        before.paste(shirt,shirt)

        before.save(sys.argv[2])




    except FileNotFoundError:
        sys.exit("Input does not exist")