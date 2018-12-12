import math
app.background = 'black'
app.stepsPerSecond = math.inf
c = Circle(200, 200, 5, fill='white')
l = Label('', 200, 200, size=24, fill='white')
def onStep():
    c.centerX = randrange(0, 400)
    c.centerY = randrange(0, 400)
    l.value = f'{c.centerX}, {c.centerY}'
