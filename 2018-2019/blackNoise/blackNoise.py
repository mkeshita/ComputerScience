app.stepsPerSecond = 60
app.background = 'black'

l = []
for i in range(0, 256):
    l.append(Line(0, 0, 1, 1))

def genClr():
    return rgb(randrange(255), randrange(255), randrange(255))
    # return gradient(
    #     rgb(randrange(255), randrange(255), randrange(255)),
    #     rgb(randrange(255), randrange(255), randrange(255))
    # )

def onStep():
    for i in l:
        r = [-50, 450]
        i.x1 = randrange(r[0], r[1]); i.y1 = randrange(r[0], r[1])
        i.x2 = randrange(r[0], r[1]); i.y2 = randrange(r[0], r[1])
        i.lineWidth = randrange(1, 4)
        i.fill = genClr()
onStep()
