app.background = 'black'; app.mem = {}
wave = Group()

app.mem['num'] = 404
app.mem['color'] = False
for i in range(50):
    wave.add(Circle(200, 200, app.mem['num'], fill=(app.mem['color'] and 'blue' or 'black')))
    if (app.mem['color'] == True): app.mem['color'] = False
    else: app.mem['color'] = True
    app.mem['num'] -= 4
    
def onStep():
    for i in wave.children:
        if (i.radius == 4): i.radius = 404; i.toBack()
        else: i.radius -= 4
