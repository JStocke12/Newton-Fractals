from PIL import Image
import cmath

width = 1024
height = 1024

coordinateWindowSize = 2.0

iterations = 10
roots = [complex(1),complex(-0.5,0.5*3**0.5),complex(-0.5,-0.5*3**0.5)]
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
        px[i,j] = tuple(int(192/([epsilon>abs(k-i) for k in newtonMethodArr].index(True)+1))+63 if epsilon>abs(newtonMethodArr[-1]-i) else 0 for i in roots)
        """if any([epsilon>abs(newtonMethodArr[-1]-i) for i in roots]):
            shade = int(192/([epsilon>abs(i-roots[0]) for i in newtonMethodArr].index(True)+1))+63
            px[i,j] = (shade,shade,shade)
        else:
            px[i,j] = (0,0,0)"""

img.save('image.png')
