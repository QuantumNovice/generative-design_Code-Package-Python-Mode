from datetime import datetime

radius = 300
segmentCount = 45

def keyReleased():
    global segmentCount
    if key == "2":
        segmentCount = 45
    elif key == "3":
        segmentCount = 24
    elif key == "4":
        segmentCount = 12
    elif key == "5":
        segmentCount = 6
    else:
        segmentCount = 360
        
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+"_##.png")   

def draw():
    global segmentCount
    colorMode(HSB, 360, width, height)
    background(360)

    angleStep = 360 / segmentCount

    beginShape(TRIANGLE_FAN)
    vertex(width/2, height/2)
    for angle in range(0, 361, angleStep):
        vx = width/2 + cos(radians(angle))*radius
        vy = height/2 + sin(radians(angle))*radius
        vertex(vx, vy)
        fill(angle, mouseX, mouseY)
    endShape()