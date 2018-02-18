add_library('generativedesign')
add_library('pdf')
import random
from datetime import datetime

tileCountX = 50
tileCountY = 10

def setup():
    global savePDF, hueValues, saturationValues, brightnessValues
    colorMode(HSB, 360, 100, 100, 100)
    noStroke()
    savePDF = False

	# create palette
    hueValues, saturationValues, brightnessValues = [], [], []
    for i in range(tileCountX):
        hueValues.append(random.randint(0,360))
        saturationValues.append(random.randint(0,100))
        brightnessValues.append(random.randint(0,10))

    
def draw():
    global savePDF, hueValues, saturationValues, brightnessValues

    # save setting
    if savePDF:
        beginRecord(PDF, datetime.now().strftime("%Y%m%d%H%M%S")+".pdf")
        colorMode(HSB, 360, 100, 100, 100)
        noStroke()

    # draw
    background(0,0,100)

    currentTileCountX = int(map(mouseX, 0, width, 1, tileCountX))
    currentTileCountY = int(map(mouseY, 0, height, 1, tileCountY))
    tileWidth = width / float(currentTileCountX)
    tileHeight = height / float(currentTileCountY)

    counter = 0
    for gridY in range(tileCountY):
        for gridX in range(tileCountX):
            posX = gridX * tileWidth
            posY = gridY * tileHeight
            index = int(counter % currentTileCountX)
            

            fill(hueValues[index],saturationValues[index],brightnessValues[index])
            rect(posX, posY, tileWidth, tileHeight)
            counter += 1
    # save
    if savePDF:
        savePDF = False
        endRecord()

def keyReleased():
    global savePDF, hueValues, saturationValues, brightnessValues
    if (key=='c' or key=='C'):
        colors = []
        for i in range(len(hueValues)):
            colors.append(color(hueValues[i],saturationValues[i],brightnessValues[i]))
        GenerativeDesign.saveASE(this, colors, datetime.now().strftime("%Y%m%d%H%M%S")+".ase")        
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+"_##.png")
    if (key=='p' or key=='P'):
        savePDF = True

    if (key == '1'):
        for i in range(tileCountX):
            hueValues[i] = random.randint(0,360)
            saturationValues[i] = random.randint(0,100)
            brightnessValues[i] = random.randint(0,100)
    if (key == '2'):
        for i in range(tileCountX):
            hueValues[i] = random.randint(0,360)
            saturationValues[i] = random.randint(0,100)
            brightnessValues[i] = 100
    if (key == '3'):  
        for i in range(tileCountX):
            hueValues[i] = random.randint(0,360)
            saturationValues[i] = 100
            brightnessValues[i] = random.randint(0,100)
    if (key == '4'):
        for i in range(tileCountX):
            hueValues[i] = 0
            saturationValues[i] = 0
            brightnessValues[i] = random.randint(0,100)
    if (key == '5'):  
        for i in range(tileCountX):
            hueValues[i] = 195
            saturationValues[i] = 100
            brightnessValues[i] = random.randint(0,100)
    if (key == '6'):
        for i in range(tileCountX):
            hueValues[i] = 195
            saturationValues[i] = random.randint(0,100)
            brightnessValues[i] = 100
    if (key == '7'):  
        for i in range(tileCountX):
            hueValues[i] = random.randint(0,180)
            saturationValues[i] = random.randint(80,100)
            brightnessValues[i] = random.randint(50,90)
    if (key == '8'): 
        for i in range(tileCountX):
            hueValues[i] = random.randint(180,360)
            saturationValues[i] = random.randint(80,100)
            brightnessValues[i] = random.randint(50,90)
    if (key == '9'):
        for i in range(tileCountX):
            if (i%2 == 0):
                hueValues[i] = random.randint(0,360)
                saturationValues[i] = 100
                brightnessValues[i] = random.randint(0,100)
            else:
                hueValues[i] = 195
                saturationValues[i] = random.randint(0,100)
                brightnessValues[i] = 100
    if (key == '0'): 
        for i in range(tileCountX):
            if (i%2 == 0):
                hueValues[i] = 192
                saturationValues[i] = random.randint(0,100)
                brightnessValues[i] = random.randint(10,100) 
            else:
                hueValues[i] = 273
                saturationValues[i] = random.randint(0,100)
                brightnessValues[i] = random.randint(10,90)
