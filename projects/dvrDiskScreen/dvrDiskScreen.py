app.background = rgb(32, 32, 32)
app.stepsPerSecond = 15
background = Rect(0, 0, 400, 300, centerY = 200)
disk = Group(
    Label('DVD', 200, 186, fill='white', size=24),
    Oval(200, 200, 50, 10, fill='white'),
    Label('VIDEO', 200, 200, size=10),
    Label('TM', 223, 205, fill='white', size=5)
)

# Hit detectors
t = Line(background.left, background.top, background.right, background.top,
    lineWidth=1, fill=None)
b = Line(background.left, background.bottom, background.right, background.bottom,
    lineWidth=1, fill=None)
l = Line(background.left, background.top, background.left, background.bottom,
    lineWidth=1, fill=None)
r = Line(background.right, background.top, background.right, background.bottom,
    lineWidth=1, fill=None)

print(' Hit Side  |   Value    | (XXX, YYY)')
print('-----------|------------|-----------')
def output(a, b, c):
    x = rounded(disk.centerX); y = rounded(disk.centerY)
    if (x < 100): x = f'0{x}'
    if (y < 100): y = f'0{y}'
    print(f'Hit {a} | {c} is now {b} | ({x}, {y})')

def changeClr():
    clr = rgb(randrange(255), randrange(255), randrange(255))
    for i in disk.children: i.fill = clr
    disk.children[2].fill = 'black'
    return clr

x = '+'; y = '+'
def onStep():
    global x; global y
    if (disk.hitsShape(t)):
        y = '+'; changeClr()
        output('top   ', y, 'y')
    if (disk.hitsShape(b)):
        y = '-'; changeClr()
        output('bottom', y, 'y')
    if (disk.hitsShape(l)):
        x = '+'; changeClr()
        output('left  ', x, 'x')
    if (disk.hitsShape(r)):
        x = '-'; changeClr()
        output('right ', x, 'x')

    speed = 3

    if (x == '+'): disk.centerX += speed
    else: disk.centerX -= speed

    if (y == '+'): disk.centerY += speed
    else: disk.centerY -= speed
