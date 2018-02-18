add_library('generativedesign')
add_library('pdf')
import random
from datetime import datetime

colorCount = 20
actRandomSeed = 0

def setup():
    global savePDF, hueValues, saturationValues, brightnessValues, actRandomSeed
    colorMode(HSB, 360, 100, 100, 100)
    noStroke()
    savePDF = False
    hueValues, saturationValues, brightnessValues = [], [], []
    
def draw():
    global savePDF, hueValues, saturationValues, brightnessValues, actRandomSeed
    background(0,0,0)
    actRandomSeed = random.randint(0, actRandomSeed)

    # save setting
    if savePDF:
        beginRecord(PDF, datetime.now().strftime("%Y%m%d%H%M%S")+".pdf")
        colorMode(HSB, 360, 100, 100, 100)
        noStroke()

    # create palette
    for i in range(colorCount):
        if (i%2 == 0):
            hueValues.append(random.randint(0,360))
            saturationValues.append(100)
            brightnessValues.append(random.randint(0,100))
        else:
            hueValues.append(195)
            saturationValues.append(random.randint(0,100))
            brightnessValues.append(100)

    counter = 0;
    rowCount = random.randint(5,40)
    rowHeight = float(height) / float(rowCount)

    for i in range(rowCount):
        # divide row
        parts = []
        for ii in range(i+1):
            if (random.random() < 0.075):
                fragments = random.randint(2,20)
                for iii in range(fragments):
                    parts.append(random.randint(0,2))
            else:
                parts.append(random.randint(2,20))

        sumPartsTotal = 0
        for ii in range(len(parts)):
            sumPartsTotal += parts[ii]

        sumPartsNow = 0
        for ii in range(len(parts)):
            sumPartsNow += parts[ii]
            if (random.random() < 0.45):
                # draw rects
                x = map(sumPartsNow, 0,sumPartsTotal, 0,width) + random.randint(-10,10)
                y = rowHeight*i + random.randint(-10,10)
                w = map(parts[ii], 0,sumPartsTotal, 0,width)*-1 + random.randint(-10,10)
                h = rowHeight*1.5

                beginShape()
                fill(0,0,0)
                vertex(x,y)
                vertex(x+w,y)

                index = counter % colorCount
                fill(hueValues[index],saturationValues[index],brightnessValues[index],25)
                vertex(x+w,y+h)
                vertex(x,y+h)
                endShape(CLOSE)
            counter += 1

    # save
    if savePDF:
        savePDF = False
        endRecord()

    noLoop()

def mouseReleased():
    global actRandomSeed
    actRandomSeed = random.randint(0, 100000)
    loop()

def keyReleased():
    global savePDF, hueValues, saturationValues, brightnessValues, actRandomSeed
    if (key=='c' or key=='C'):
        colors = []
        for i in range(len(hueValues)):
            colors.append(color(hueValues[i],saturationValues[i],brightnessValues[i]))
        GenerativeDesign.saveASE(this, colors, datetime.now().strftime("%Y%m%d%H%M%S")+".ase")        
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+"_##.png")
    if (key=='p' or key=='P'):
        savePDF = True