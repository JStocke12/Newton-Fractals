from PIL import Image

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
        newtonMethodArr = [z := complex((2*i/width-1)*coordinateWindowSize,(1-2*j/width)*coordinateWindowSize)] + [z := (z-(z**3-1)/(3*z**2) if z != complex(0) else 0) for i in range(iterations)]
        px[i,j] = tuple(int(192/([epsilon>abs(k-i) for k in newtonMethodArr].index(True)+1))+63 if epsilon>abs(newtonMethodArr[-1]-i) else 0 for i in roots)

img.save('image.png')
