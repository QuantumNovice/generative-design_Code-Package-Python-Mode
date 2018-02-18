add_library('generativedesign')
add_library('pdf')
from datetime import datetime

def setup():
    global IMG, sortMode, savePDF, colors
    IMG = loadImage("pic1.jpg")
    sortMode = None
    savePDF = False
    colors = None

    colorMode(HSB, 360, 100, 100, 100)
    noStroke()
    noCursor()

    
def draw():
    global IMG, sortMode, savePDF, colors

    # save setting
    if savePDF:
        beginRecord(PDF, datetime.now().strftime("%Y%m%d%H%M%S")+".pdf")
        colorMode(HSB, 360, 100, 100, 100)
        noStroke()

    # draw
    tileCount = width / max(mouseX, 5)
    rectSize = width / float(tileCount)
    colors = [None]*tileCount*tileCount

    i = 0
    for gridY in range(tileCount):
        for gridX in range(tileCount):
            px = int(gridX * rectSize)
            py = int(gridY * rectSize)
            colors[i] = IMG.get(px, py)
            i += 1

    if sortMode != None:
        colors = GenerativeDesign.sortColors(this, colors, sortMode)

    i = 0
    for gridY in range(tileCount):
        for gridX in range(tileCount):
            fill(colors[i])
            rect(gridX*rectSize, gridY*rectSize, rectSize, rectSize)
            i += 1

    # save
    if savePDF:
        savePDF = False
        endRecord()

def keyReleased():
    global IMG, sortMode, savePDF, colors

    if (key=='c' or key=='C'):
        GenerativeDesign.saveASE(this, colors, datetime.now().strftime("%Y%m%d%H%M%S")+".ase")
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+"_##.png")
    if (key=='p' or key=='P'):
        savePDF = True

    if (key == '1'):
        IMG = loadImage("pic1.jpg")
    if (key == '2'):
        IMG = loadImage("pic2.jpg")
    if (key == '3'):
        IMG = loadImage("pic3.jpg")
    if (key == '4'):
        sortMode = None
    if (key == '5'):
        sortMode = GenerativeDesign.HUE
    if (key == '6'):
        sortMode = GenerativeDesign.SATURATION
    if (key == '7'):
        sortMode = GenerativeDesign.BRIGHTNESS
    if (key == '8'):
        sortMode = GenerativeDesign.GRAYSCALE