### Imports
import math

### App Setup
app.background = 'black'
app.stepsPerSecond = 60
Label('Not to Scale!', app.right - 5, app.bottom - 5,
    fill='white', align='bottom-right',
    size=10, opacity=50)

### Star Generator
stars = []
for i in range(200):
    stars.append(Circle(randrange(400), randrange(400), 1, fill='white'))
Circle(200, 200, 35, fill=gradient('darkRed', 'yellow'))

### Planet Generator
def newPlt(x, r, c):
    Circle(app.centerX, app.centerY, x+r, fill=None,
        border='lightCyan', borderWidth=r*2, opacity=10)
    return Circle(x + app.centerX, app.centerY, r, fill=c)

planets = {
    "mercury": newPlt(42, 3, 'grey'),
    "venus": newPlt(52, 4, 'peachPuff'),
    "earth": newPlt(65, 5, 'skyblue'),
    "mars": newPlt(78, 4, 'salmon'),
    "jupiter": newPlt(107, 20, 'ivory'),
    "saturn":  newPlt(145, 15, 'sandyBrown'),
    "uranus": newPlt(171, 8, 'aliceBlue'),
    "neptune": newPlt(188, 7, 'blue'),
    "pluto": newPlt(198, 1, 'silver')
}

### Setup Speed and Shadow
for p in planets.values():
    p.distFromSun = p.centerX - app.centerX
    p.speed = math.pow(-150, 9)/math.pow(p.centerX, 8)
    p.shadow = Line(app.centerX, app.centerY, p.centerX, p.centerY,
        lineWidth=p.radius*2, opacity=50)

### Movement Handler
app.steps = randrange(999999999)
def onStep():
    app.steps += 1
    for i in stars:
        i.radius = randrange(1, 3)
    for p in planets.values():
        # Thanks Bryan for the Trig help! 😁
        p.centerX = math.cos((app.steps*p.speed)/app.stepsPerSecond)*p.distFromSun+200
        p.centerY = math.sin((app.steps*p.speed)/app.stepsPerSecond)*p.distFromSun+200
        p.shadow.x2 = (p.centerX*10)-1800; p.shadow.y2 = (p.centerY*10)-1800
        p.shadow.x1 = p.centerX; p.shadow.y1 = p.centerY
