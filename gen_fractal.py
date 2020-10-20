from PIL import Image

width = 256
height = 256

coordinateWindowSize = 2.0

img = Image.new('RGB', (width, height))

px = img.load()

for i in range(width):
    for j in range(height):
        x = (2*i/width-1)*coordinateWindowSize
        y = (2*j/width-1)*coordinateWindowSize
        px[i,j] = ((256*x^2)%256,(256*y^2)%256,0)

img.save('image.png')
