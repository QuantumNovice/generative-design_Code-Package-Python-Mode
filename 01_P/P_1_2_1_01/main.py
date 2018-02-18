from datetime import datetime

MAX_TILECOUNT_Y = 10
COLORSLEFT, COLORSRIGHT = [], []

def shakeColors():
    global COLORSLEFT, COLORSRIGHT
    COLORSLEFT, COLORSRIGHT = [], []
    for i in range(MAX_TILECOUNT_Y):
        COLORSLEFT.append(color(random(0,60), random(0,100), 100))
        COLORSRIGHT.append(color(random(160,190), 100, random(0,100)))

def mouseReleased():
    shakeColors()

def keyReleased():
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+"_##.png")
        
def setup():
    background(0)
    colorMode(HSB, 360, 100, 100, 100)
    noStroke()
    shakeColors()
 
def draw():
    tileCountX = int(map(mouseX, 0, width, 2, 100))
    tileCountY = int(map(mouseY, 0, height, 2, MAX_TILECOUNT_Y))
    tileWidth = width / tileCountX
    tileHeight = height / tileCountY

    for gridY in range(tileCountY):
        col1 = COLORSLEFT[gridY]
        col2 = COLORSRIGHT[gridY]
        for gridX in range(tileCountX):
            amount = map(gridX, 0, tileCountX-1, 0, 1)
            interCol = lerpColor(col1, col2, amount)

            posX = tileWidth*gridX
            posY = tileHeight*gridY
            fill(interCol)
            rect(posX, posY, tileWidth, tileHeight)
            