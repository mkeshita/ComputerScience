app.background = 'black'; app.mem = {}
wave = Group()

app.mem['num'] = 0
for i in range(101):
    wave.add(Line(app.mem['num'], 0, app.mem['num'], 400,
        fill=gradient('black', 'yellow', 'red', start='bottom'),
        lineWidth=4, dashes=True))
    app.mem['num'] += 4
    
def onStep():
    for i in wave.children:
        i.y1 = randrange(400)
