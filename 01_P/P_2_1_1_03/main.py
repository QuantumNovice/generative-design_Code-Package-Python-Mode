add_library('pdf')
import random
from datetime import datetime

def setup():
    global savePDF, tileCount, actRandomSeed, transparentLeft, transparentRight
    global alphaLeft, alphaRight, colorBack, colorLeft, colorRight
    savePDF = False

    tileCount = 1
    actRandomSeed = 0
    transparentLeft = False
    transparentRight = False

    alphaLeft = 100
    alphaRight = 100

    colorBack = color(255)
    colorLeft = color(0)
    colorRight = color(0)

def draw():
    global savePDF, tileCount, actRandomSeed, transparentLeft, transparentRight
    global alphaLeft, alphaRight, colorBack, colorLeft, colorRight
    if savePDF:
        beginRecord(PDF, datetime.now().strftime("%Y%m%d%H%M%S")+".pdf")

    colorMode(HSB, 360, 100, 100, 100)
    background(colorBack)
    smooth()
    noFill()
    random.seed(actRandomSeed)
    strokeWeight(mouseX/15);

    tileCount = mouseY/15;

    for gridY in range(tileCount):
        for gridX in range(tileCount):
            posX = int(width/tileCount*gridX)
            posY = int(height/tileCount*gridY)

            if (transparentLeft == True):
                alphaLeft = gridY*10
            else:
                alphaLeft = 100

            if (transparentRight == True):
                alphaRight = 100-gridY*10
            else:
                alphaRight = 100

            toggle = random.randint(0,1)

            if (toggle == 0):
                stroke(colorLeft, alphaLeft)
                line(posX, posY, posX+(width/tileCount)/2, posY+height/tileCount)
                line(posX+(width/tileCount)/2, posY, posX+(width/tileCount), posY+height/tileCount)
            elif  (toggle == 1):
                stroke(colorRight, alphaRight)
                line(posX, posY+width/tileCount, posX+(height/tileCount)/2, posY)
                line(posX+(height/tileCount)/2, posY+width/tileCount, posX+(height/tileCount), posY)

        if (savePDF):
            savePDF = False
            endRecord()

def mousePressed():
    global savePDF, tileCount, actRandomSeed, transparentLeft, transparentRight
    global alphaLeft, alphaRight, colorBack, colorLeft, colorRight
    actRandomSeed = random.randint(0, 100000)


def keyReleased():
    global savePDF, tileCount, actRandomSeed, transparentLeft, transparentRight
    global alphaLeft, alphaRight, colorBack, colorLeft, colorRight
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+".png")
    if (key=='p' or key=='P'):
        savePDF = True

    if (key == '1'):
        if (colorLeft == color(273, 73, 51)):
            colorLeft = color(323, 100, 77)
        else:
            colorLeft = color(273, 73, 51)
    elif (key == '2'):
        if (colorRight == color(0)):
            colorRight = color(192, 100, 64)
        else:
            colorRight = color(0)
    elif (key == '3'):
        transparentLeft = not(transparentLeft)
    elif (key == '4'):
        transparentRight = not(transparentRight)
    
    if (key == '0'):
        transparentLeft = False
        transparentRight = False
        colorLeft = color(323, 100, 77)
        colorRight = color(0)
