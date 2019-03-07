app.stepsPerSecond = 60
app.background = 'black'
pac = Circle(200, 200, 35, fill='gold')
pacM = RegularPolygon(pac.centerX + 28, 200, 35/2, 3, rotateAngle=-90)

def onKeyHold(k):
    if ('up' in k):
        pac.centerY -= 1
        pacM.centerX = pac.centerX
        pacM.centerY = pac.centerY - 28
        pacM.rotateAngle = 180
    if ('down' in k):
        pac.centerY += 1
        pacM.centerX = pac.centerX
        pacM.centerY = pac.centerY + 28
        pacM.rotateAngle = 0
    if ('left' in k):
        pac.centerX -= 1
        pacM.centerX = pac.centerX - 28
        pacM.centerY = pac.centerY
        pacM.rotateAngle = 90
    if ('right' in k):
        pac.centerX += 1
        pacM.centerX = pac.centerX + 28
        pacM.centerY = pac.centerY
        pacM.rotateAngle = -90
