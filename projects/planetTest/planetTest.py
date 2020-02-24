import math
# Settings ##################
app.background = 'black'
app.stepsPerSecond = 60 # The framerate of the app.
app.steps = 0 # The default steps.

obj = {
    'sun': Circle(app.centerX, app.centerY, 25, fill=gradient('darkRed', 'yellow')),
    'plt': Circle(325, 200, 12.5, fill='skyblue'),
    'mun': Circle(370, 200, 6.25, fill='grey')
}

obj['plt'].distFromSun = obj['plt'].centerX - app.centerX
obj['mun'].distFromPlt = obj['mun'].centerX - obj['plt'].centerX
obj['plt'].speed = -1
obj['mun'].speed = -5

def onStep():
    app.steps += 1
    p = obj['plt']
    p.centerX = math.cos((app.steps*p.speed)/app.stepsPerSecond)*p.distFromSun+200
    p.centerY = math.sin((app.steps*p.speed)/app.stepsPerSecond)*p.distFromSun+200

    m = obj['mun']
    m.centerX = math.sin((app.steps*m.speed)/app.stepsPerSecond)*m.distFromPlt+p.centerX
    m.centerY = math.cos((app.steps*m.speed)/app.stepsPerSecond)*m.distFromPlt+p.centerY
