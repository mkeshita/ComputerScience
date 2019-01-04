import math
d = Circle(200, 200, 15, fill='red')

# Settings ##################
app.radius = 30 # The default radius.
app.center = [200, 200] # The default start location.
app.stepsPerSecond = 60 # The framerate of the app.
app.steps = 0 # The default steps.
app.speed = -15

def onStep():
    d.centerX = math.sin((app.steps*app.speed)/app.stepsPerSecond)*app.radius+app.center[0]
    d.centerY = math.cos((app.steps*app.speed)/app.stepsPerSecond)*app.radius+app.center[1]
    app.steps += 1

def onMouseMove(x, y):
    app.center = [x, y]

def onKeyPress(k):
    if (k == 'up'): app.radius += 5
    if (k == 'down'): app.radius -= 5
