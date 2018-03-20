add_library('pdf')
from datetime import datetime

def setup():
    global recordPDF
    recordPDF = False
    smooth()
    noFill()
    background(255)

def draw():
    global recordPDF
    if(mousePressed):
        pushMatrix()
        translate(width/2,height/2)

        circleResolution = int(map(mouseY+100,0,height,2, 10))
        radius = mouseX-width/2 + 0.5
        angle = TWO_PI/circleResolution

        strokeWeight(2)
        stroke(0, 25)

        beginShape()
        for i in range(circleResolution+1):
            x = 0 + cos(angle*i) * radius
            y = 0 + sin(angle*i) * radius
            vertex(x, y)
        endShape()
        popMatrix()

def keyReleased():
    global recordPDF
    if (key == DELETE or key == BACKSPACE):
        background(255)
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+".png")

    # pdf export
    if (key =='r' or key =='R'):
        if (recordPDF == False):
            beginRecord(PDF, datetime.now().strftime("%Y%m%d%H%M%S")+".pdf")
            println("recording started")
            recordPDF = True
            smooth()
            noFill()
            background(255)
    elif (key == 'e' or key =='E'):
        if (recordPDF):
            println("recording stopped")
            endRecord()
            recordPDF = False
            background(255)
