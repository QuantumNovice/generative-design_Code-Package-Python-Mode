from datetime import datetime

def setup():
    background(0)

def draw():
    colorMode(HSB, width, height, 100)
    stepX = mouseX+2
    stepY = mouseY+2

    for gridY in range(0, height, stepY):
        for gridX in range(0, width, stepX):
            rect(gridX, gridY, stepX, stepY)
            fill(gridX, height-gridY, 100)
            
def keyReleased():
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+"_##.png")