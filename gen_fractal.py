from PIL import Image
import cmath

width = 1024
height = 1024

coordinateWindowSize = 2.0

iterations = 10
roots = [complex(1),complex(-0.5,1.5**0.5),complex(-0.5,-(1.5**0.5))]
epsilon = 0.1

img = Image.new('RGB', (width, height))

px = img.load()

for i in range(width):
    for j in range(height):
        x = (2*i/width-1)*coordinateWindowSize
        y = (1-2*j/width)*coordinateWindowSize
        newtonMethodArr = [complex(x,y)]
        for k in range(iterations):
            newtonMethodArr.append(newtonMethodArr[-1]-(newtonMethodArr[-1]**3-1)/(3*newtonMethodArr[-1]**2) if newtonMethodArr[-1] != complex(0) else 0)
        if any([epsilon>abs(newtonMethodArr[-1]-i) for i in roots]):
            px[i,j] = (255,255,255)
        else:
            px[i,j] = (0,0,0)

img.save('image.png')
