app.stepsPerSecond = 1
app.background = 'darkSlateGray'

# Clock group and face.
clock = Group(
    Circle(200, 200, 200, fill=None, border='white', borderWidth=6),
    Circle(200, 200, 4, fill='white')
)

# Hands
def hands(h):
    g = Group()
    for i in h:
        l = Line(
            200, 200, 200, i, fill='white',
            opacity=50, lineWidth=4, arrowEnd=False
        )
        l.l = 200 - i; g.add(l)
    clock.add(g)
hands([25, 50, 100])

# Points
def points(a):
    g = Group()
    r = 360 / a
    for i in range(a):
        x1, y1 = getPointInDir(200, 200, r*i, 180)
        x2, y2 = getPointInDir(200, 200, r*i, 200)
        g.add(Line(x1, y1, x2, y2, fill='white', lineWidth=8, opacity=50))
    clock.add(g)
points(12)

time = 1
def onStep():
    global time
    # if (time >= 3600*12): time = 0
    a = [time*6, (time/60)*6, (time/60/60)*(6*5)]
    for i in range(3):
        h = clock.children[2].children[i]
        x, y = getPointInDir(200, 200, a[i], h.l)
        h.x2 = x; h.y2 = y
    time += 1
