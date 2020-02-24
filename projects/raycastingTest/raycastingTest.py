import math
import time
app.setMaxShapeCount(math.inf)
app.stepsPerSecond = math.inf
app.seed = randrange(int('1' + ('0' * 12)))
seed(567597381855)
print(app.seed)  # app.seed is default.
# 23378241, 811041673, 567597381855

### Generate Pixels
l = makeList(50, 50)
for x in range(len(l)):
    for y in range(len(l[x])):
        r = app.right / len(l)
        c = app.bottom / len(l[x])
        l[x][y] = Rect(r*x, c*y, r, c)

### Generate Shapes
ss = Group()
for i in range(3):
    c = choice(['r', 'p', 'c'])
    def ri(n1, n2): return randrange(n1, n2+1)

    x = ri(app.left, app.right)
    y = ri(app.top, app.bottom)
    r = ri(50, 100)
    if (c == 'r'):
        s = Rect(x, y, ri(25, 100), ri(25, 100))
    if (c == 'p'):
        s = RegularPolygon(x, y, r, choice([3, 5]))
    if (c == 'c'):
        s = Circle(x, y, r)

    s.dr = ri(-5, 5)
    s.dx = ri(-2, 2)
    s.dy = ri(-2, 2)
    s.fill = rgb(ri(0, 255), ri(0, 255), ri(0, 255))
    s.f = s.fill
    s.rotateAngle = ri(0, 360)
    s.opacity = 0
    ss.add(s)


def b(a, o):
    if (a == 'space'):
        if (o == 1):
            for i in ss.children:
                i.fill = None
                i.border = i.f
        else:
            for i in ss.children:
                i.fill = i.f
                i.border = None


def onKeyPress(k): b(k, 1)


def onKeyRelease(k): b(k, 0)


steps = 0
oldT = time.time()
fps = Label(0, app.right - 30, app.bottom - 20,
            fill='lime', font='monospace', size=32)


def onStep():
    global steps
    global oldT
    steps += 1
    if (time.time() - oldT >= 1):
        fps.value = steps
        steps = 0
        oldT = time.time()

    for s in ss:
        s.centerX += s.dx
        s.centerY += s.dy
        s.rotateAngle += s.dr
        if (s.rotateAngle >= 360 or s.rotateAngle <= -360):
            s.rotateAngle = 0
        if (s.top > app.bottom):
            s.bottom = app.top
        if (s.bottom < app.top):
            s.top = app.bottom
        if (s.left > app.right):
            s.right = app.left
        if (s.right < app.left):
            s.left = app.right

    for c in l:
        for i in c:
            i.fill = 'black'
    for c in l:
        for i in c:
            for s in ss:
                if i.hitsShape(s):
                    i.fill = s.f
