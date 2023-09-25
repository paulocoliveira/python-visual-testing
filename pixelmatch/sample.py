from PIL import Image

from pixelmatch.contrib.PIL import pixelmatch

image1 = Image.open('../images/image1.jpg')
image2 = Image.open('../images/image2.jpg')
img_diff = Image.new("RGBA", image1.size)

# note how there is no need to specify dimensions
mismatch = pixelmatch(image1, image2, img_diff, includeAA=True)

img_diff.save('../images/pixelmatchdiff.png')