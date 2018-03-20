add_library('pdf')
from datetime import datetime

def setup():
    global savePDF
    savePDF = False
    
def draw():
    global savePDF

    if savePDF:
        beginRecord(PDF, datetime.now().strftime("%Y%m%d%H%M%S")+".pdf")

    strokeCap(SQUARE)
    smooth()
    noFill()
    background(255)
    translate(width/2,height/2)

    circleResolution = int(map(mouseY, 0,height, 2,80))
    radius = mouseX-width/2 + 0.5
    angle = TWO_PI/circleResolution

    strokeWeight(mouseY/20)

    beginShape()
    for i in range(circleResolution):
        x = cos(angle*i) * radius
        y = sin(angle*i) * radius
        line(0, 0, x, y)
        #vertex(x, y)
    endShape()

    if savePDF:
        savePDF = False
        endRecord()

def keyReleased():
    global savePDF
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+".png")
    if (key=='p' or key=='P'):
        savePDF = True