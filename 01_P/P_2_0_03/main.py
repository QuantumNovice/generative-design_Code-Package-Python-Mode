add_library('pdf')
from datetime import datetime

def setup():
    global recordPDF, strokeColor
    recordPDF = False
    strokeColor = color(0, 10)
    colorMode(HSB, 360, 100, 100, 100);
    smooth()
    noFill()
    background(360)

def draw():
    global recordPDF, strokeColor
    if(mousePressed):
        pushMatrix()
        translate(width/2,height/2)

        circleResolution = int(map(mouseY+100,0,height,2, 10))
        radius = mouseX-width/2 + 0.5
        angle = TWO_PI/circleResolution

        strokeWeight(2)
        stroke(strokeColor)

        beginShape()
        for i in range(circleResolution+1):
            x = 0 + cos(angle*i) * radius
            y = 0 + sin(angle*i) * radius
            vertex(x, y)
        endShape()
        popMatrix()

def keyReleased():
    global recordPDF, strokeColor
    if (key == DELETE or key == BACKSPACE):
        background(255)
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+".png")

    if key == "1":
        strokeColor = color(0, 10)
    elif key == "2":
        strokeColor = color(192, 100, 64, 10)
    elif key == "3":
        strokeColor = color(52, 100, 71, 10)

    # pdf export
    if (key =='r' or key =='R'):
        if (recordPDF == False):
            beginRecord(PDF, datetime.now().strftime("%Y%m%d%H%M%S")+".pdf")
            println("recording started")
            recordPDF = True
            colorMode(HSB, 360, 100, 100, 100)
            smooth()
            noFill()
            background(360)
    elif (key == 'e' or key =='E'):
        if (recordPDF):
            println("recording stopped")
            endRecord()
            recordPDF = False
            background(c60)
