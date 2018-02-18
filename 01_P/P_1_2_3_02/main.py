add_library('generativedesign')
add_library('pdf')
import random
from datetime import datetime

colorCount = 20

def setup():
    global savePDF, hueValues, saturationValues, brightnessValues
    colorMode(HSB, 360, 100, 100, 100)
    noStroke()
    savePDF = False
    hueValues, saturationValues, brightnessValues = [], [], []
    
def draw():
    global savePDF, hueValues, saturationValues, brightnessValues

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
                    parts.append(random.randint(0,5))
            else:
                parts.append(random.randint(2,20))

        sumPartsTotal = 0
        for ii in range(len(parts)):
            sumPartsTotal += parts[ii]

        # draw rects
        sumPartsNow = 0
        for ii in range(len(parts)):
            index = counter % colorCount
            fill(hueValues[index],saturationValues[index],brightnessValues[index])

            sumPartsNow += parts[ii]
            rect(map(sumPartsNow, 0,sumPartsTotal, 0,width),  # x
                 rowHeight*i,                                 # y
                 map(parts[ii], 0,sumPartsTotal, 0,width)*-1, # width
                 rowHeight)                                   # height
            counter += 1

    # save
    if savePDF:
        savePDF = False
        endRecord()

    noLoop()

def mouseReleased():
    loop()

def keyReleased():
    global savePDF, hueValues, saturationValues, brightnessValues
    if (key=='c' or key=='C'):
        colors = []
        for i in range(len(hueValues)):
            colors.append(color(hueValues[i],saturationValues[i],brightnessValues[i]))
        GenerativeDesign.saveASE(this, colors, datetime.now().strftime("%Y%m%d%H%M%S")+".ase")        
    if (key=='s' or key=='S'):
        saveFrame(datetime.now().strftime("%Y%m%d%H%M%S")+"_##.png")
    if (key=='p' or key=='P'):
        savePDF = True
