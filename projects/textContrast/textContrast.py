app.background = rgb(153, 170, 181)  # Discord Greyple Color Lol
block = Rect(0, 0, 250, 150); block.centerX = app.centerX; block.centerY = app.centerY/2
sampleTxt = Label('Sample Text', block.centerX, block.centerY, size=32)

def getPercent(mn, mx, val): return (1/(mx-mn))*(val-mn)
def getValue(mn, mx, val): return (val)*(mx-mn)+(mn)

### Generate Slider
def genSlider(x, y, f):
    vert = Line(
        x, y-85, x, y+85,
        lineWidth=8, fill=f
    )
    flat = Line(
        vert.centerX-20, vert.bottom,
        vert.centerX+20, vert.bottom,
        lineWidth=16, fill=f
    )
    lbl = Label(0, x, y - 105, size=16)
    g = Group(vert, flat, lbl); g.grabbed = False
    return g

### Slider List
sliders = [
    genSlider((400/4)*1, 300, 'red'),
    genSlider((400/4)*2, 300, 'green'),
    genSlider((400/4)*3, 300, 'blue')
]

### Calculate Text Contrast
def textContrast(r, g, b):
    i = (r*0.299 + g*0.587 + b*0.114)
    if (i >= 148): return 'black'
    else: return 'white'

### Set Random Color
def randomizeColor():
    def f(): return randrange(256)
    r = f(); g = f(); b = f()
    block.fill = rgb(r, g, b); sampleTxt.fill = textContrast(r, g, b)
    clrs = [r, g, b]
    for itvl in range(3):
        sliders[itvl].children[1].centerY = getValue(
            sliders[itvl].children[0].top,
            sliders[itvl].children[0].bottom,
            getPercent(0, 255, clrs[itvl])
        ); sliders[itvl].children[2].value = clrs[itvl]
randomizeColor()

### Slider Limiter
def limiter(g, i):
    return {
        i < g.children[0].top: g.children[0].top,
        i > g.children[0].bottom: g.children[0].bottom
    }.get(True, i)

def sliderMoved(i, y):
    y = limiter(i, y)
    cc = rounded(255*(1-getPercent(i.children[0].top, i.children[0].bottom, y)))
    i.children[1].centerY = y
    i.children[2].value = cc
    if (i.children[0].fill == 'red'): block.fill = rgb(cc, block.fill.green, block.fill.blue)
    if (i.children[0].fill == 'green'): block.fill = rgb(block.fill.red, cc, block.fill.blue)
    if (i.children[0].fill == 'blue'): block.fill = rgb(block.fill.red, block.fill.green, cc)
    sampleTxt.fill = textContrast(block.fill.red, block.fill.green, block.fill.blue)

def onMousePress(x, y):
    if (block.contains(x, y)): randomizeColor()
    for i in sliders:
        if (i.contains(x, y)):
            i.grabbed = True
            sliderMoved(i, y)

def onMouseRelease(x, y):
    for i in sliders:
        i.grabbed = False

def onMouseDrag(x, y):
    for i in sliders:
        if (i.grabbed):
            sliderMoved(i, y)
