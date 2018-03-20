add_library('pdf')
import random
from datetime import datetime


tileCount = 20

def setup():
    global savePDF, actStrokeCap, actRandomSeed, colorLeft, colorRight, alphaLeft, alphaRight
    savePDF = False
    actStrokeCap = ROUND
    actRandomSeed = 0
    colorLeft = color(197, 0, 123)
    colorRight = color(87, 35, 129)
    alphaLeft = 100
    alphaRight = 100

def draw():
    global savePDF, actStrokeCap, actRandomSeed, colorLeft, colorRight, alphaLeft, alphaRight

    if savePDF:
        beginRecord(PDF, datetime.now().strftime("%Y%m%d%H%M%S")+".pdf")

    background(255)
    smooth()
    noFill()
    strokeCap(actStrokeCap)
    
    random.seed(actRandomSeed)

    for gridY in range(tileCount):
        for gridX in range(tileCount):
            posX = int(width/tileCount*gridX)
            posY = int(height/tileCount*gridY)

            toggle = random.randint(0,1)

            if (toggle == 0):
                strokeWeight(mouseX/20)
                stroke(colorLeft, alphaLeft)
                line(posX, posY, posX+width/tileCount, posY+height/tileCount)
            elif  (toggle == 1):
                strokeWeight(mouseY/20)
                stroke(colorRight, alphaRight)
                line(posX, posY+width/tileCount, posX+height/tileCount, posY)

        if (savePDF):
            savePDF = False
            endRecord()

def mousePressed():
    global savePDF, actStrokeCap, actRandomSeed, colorLeft, colorRight, alphaLeft, alphaRight
    actRandomSeed = random.randint(0, 100000)


def keyReleased():
    global savePDF, actStrokeCap, actRandomSeed, colorLeft, colorRight, alphaLeft, alphaRight
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+".png")
    if (key=='p' or key=='P'):
        savePDF = True

    if key == "1":
        actStrokeCap = ROUND
    elif key == "2":
        actStrokeCap = SQUARE
    elif key == "3":
        actStrokeCap = PROJECT
    elif (key == '4'):
        if (colorLeft == color(0)):
            colorLeft = color(323, 100, 77)
        else:
            colorLeft = color(0)
    elif (key == '5'):
        if (colorRight == color(0)):
            colorRight = color(273, 73, 51)
        else:
            colorRight = color(0)
    elif (key == '6'):
        if (alphaLeft == 100):
            alphaLeft = 50
        else:
            alphaLeft = 100
    elif (key == '7'):
        if (alphaRight == 100):
            alphaRight = 50
        else:
            alphaRight = 100
    
    if (key == '0'):
        actStrokeCap = ROUND
        colorLeft = color(0)
        colorRight = color(0)
        alphaLeft = 100
        alphaRight = 100
