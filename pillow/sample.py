from PIL import Image, ImageChops

image1 = Image.open('../images/image1.jpg')
image2 = Image.open('../images/image3.jpg')
diff = ImageChops.difference(image1, image2)
diff.save("../images/pillowdiff.png")