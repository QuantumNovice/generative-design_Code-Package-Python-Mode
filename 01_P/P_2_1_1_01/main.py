add_library('pdf')
import random
from datetime import datetime


tileCount = 20

def setup():
    global savePDF, actStrokeCap, actRandomSeed
    savePDF = False
    actStrokeCap = ROUND
    actRandomSeed = 0

def draw():
    global savePDF, actStrokeCap, actRandomSeed

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
                line(posX, posY, posX+width/tileCount, posY+height/tileCount)
            elif  (toggle == 1):
                strokeWeight(mouseY/20)
                line(posX, posY+width/tileCount, posX+height/tileCount, posY)

        if (savePDF):
            savePDF = False
            endRecord()

def mousePressed():
    global savePDF, actStrokeCap, actRandomSeed
    actRandomSeed = random.randint(0, 100000)


def keyReleased():
    global savePDF, actStrokeCap, actRandomSeed
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

