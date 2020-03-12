app.background = rgb(153, 170, 181)
s = Rect(0, 0, 250, 150); s.centerX = app.centerX; s.centerY = app.centerY
l = Label('Sample Text', s.centerX, s.centerY, size=32)

def textContrast(r, g, b):
    i = (r*0.299 + g*0.587 + b*0.114)
    if (i >= 128): return 'black'
    else: return 'white'

def onMousePress(x, y):
    if (s.contains(x, y)):
        def f(): return randrange(256)
        r = f(); g = f(); b = f()
        s.fill = rgb(r, g, b)
        l.fill = textContrast(r, g, b)
onMousePress(app.centerX, app.centerY)
