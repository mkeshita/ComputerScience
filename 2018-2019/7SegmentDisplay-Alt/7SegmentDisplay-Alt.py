app.background = rgb(32, 32, 32)

### Triangle and Rectangle Generator.
def tri(x, y, dir): return RegularPolygon(x, y, 7, 3,
    fill='white', border='white', borderWidth=0.25, rotateAngle=dir * 90)
def rec(a):
    if (a): return Rect(0, 0, 37, 12, fill='white', border='white', borderWidth=0.25)
    else: return Rect(0, 0, 12, 37, fill='white', border='white', borderWidth=0.25)

### Segment Generator using Triangles and Rectangles.
def flat(): return Group(tri(-4, 6, 3), rec(True), tri(41, 6, 1))
def vert(): return Group(tri(6, -4, 0), rec(False), tri(6, 41, 2))

### Generate a full 7-Segment Display.
def genSeg(x, y):
    # Allign each segment to assemble a display.
    a = flat(); a.centerX = x; a.centerY = y - 60
    b = vert(); b.centerX = x + 30; b.centerY = y - 30
    c = vert(); c.centerX = x + 30; c.centerY = y + 30
    d = flat(); d.centerX = x; d.centerY = y + 60
    e = vert(); e.centerX = x - 30; e.centerY = y + 30
    f = vert(); f.centerX = x - 30; f.centerY = y - 30
    g = flat(); g.centerX = x; g.centerY = y
    return Group(a, b, c, d, e, f, g)

a = genSeg(100, 100); b = genSeg(300, 100)
c = genSeg(200, 200)
d = genSeg(100, 300); e = genSeg(300, 300)

def init():
    if (a.rotateAngle == 0): a.rotateAngle = 90
    else: a.rotateAngle = 0
    if (b.rotateAngle == 0): b.rotateAngle = 90
    else: b.rotateAngle = 0
    if (c.rotateAngle == 0): c.rotateAngle = 90
    else: c.rotateAngle = 0
    if (d.rotateAngle == 0): d.rotateAngle = 90
    else: d.rotateAngle = 0
    if (e.rotateAngle == 0): e.rotateAngle = 90
    else: e.rotateAngle = 0
def onMousePress(x, y): init()
def onMouseRelease(x, y): init()

### Create a watermark label as a global variable and edit the properties.
l = Label('7-Segment Display', 200, 200)
l.fill='lightgrey'; l.border='black'
l.borderWidth = 1; l.size=50; l.rotateAngle = 45
