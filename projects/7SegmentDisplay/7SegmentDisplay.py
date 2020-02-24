import math
app.stepsPerSecond = 2
app.background = 'black'

class Seg:
    def __init__(self, x, y):
        def genTri(x, y, dir): return RegularPolygon(x, y, 7, 3, fill='white', border='white', borderWidth=0.25, rotateAngle=dir * 90)
        def genRec(ang): return Rect(0, 0, ang and 37 or 12, ang and 12 or 37, fill='white', border='white', borderWidth=0.25)
        def flat(): return Group(genTri(-4, 6, 3), genRec(True), genTri(41, 6, 1))
        def vert(): return Group(genTri(6, -4, 0), genRec(False), genTri(6, 41, 2))
        a = flat(); a.centerX = x; a.centerY = y - 60
        b = vert(); b.centerX = x + 30; b.centerY = y - 30
        c = vert(); c.centerX = x + 30; c.centerY = y + 30
        d = flat(); d.centerX = x; d.centerY = y + 60
        e = vert(); e.centerX = x - 30; e.centerY = y + 30
        f = vert(); f.centerX = x - 30; f.centerY = y - 30
        g = flat(); g.centerX = x; g.centerY = y
        self.groups = Group(a, b, c, d, e, f, g)
        self.value = 8
    def changeValue(self, v):
        if v not in [None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            raise ValueError(f'\'{v}\' is not a valid single digit number.')
        d = ['0', '1', '2', '3', '4', '5', '6']
        posValues = {
            None: [],
            'all': [0, 1, 2, 3, 4, 5, 6],
            0: [0, 1, 2, 3, 4, 5],
            1: [1, 2],
            2: [0, 1, 3, 4, 6],
            3: [0, 1, 2, 3, 6],
            4: [1, 2, 5, 6],
            5: [0, 2, 3, 5, 6],
            6: [0, 2, 3, 4, 5, 6],
            7: [0, 1, 2],
            8: [0, 1, 2, 3, 4, 5, 6],
            9: [0, 1, 2, 5, 6]
        }
        for i in posValues[v]:
            d.remove(str(i))
            for s in self.groups.children[i].children:
                s.fill = 'white'
        for i in d:
            for s in self.groups.children[int(i)].children:
                s.fill = None
        self.value = v
### End Class
segments = {
    'minutes': [Seg(50, 200), Seg(140, 200)],
    'seconds': [Seg(260, 200), Seg(350, 200)]
}
colon = Group(
    Rect(193, 165, 15, 15, fill='white', opacity=0),
    Rect(193, 225, 15, 15, fill='white', opacity=0)
)
for s in segments.values():
    s.reverse()
    for i in s:
        i.changeValue(0)

time = 2; l = Label('', 200, 395, fill='white', font='monospace', bold=True, opacity=50)
def onStep():
    global time
    if (time % 2 == 0):
        for i in colon.children: i.opacity = 100
        secs = list(str(math.floor((time / 2) % 60))); secs.reverse()
        mins = list(str(math.floor((time / 2 / 60) % 60))); mins.reverse()
        print(time, ''.join(mins), ''.join(secs))
        index = -1

        for i in range(0, 2):
            index += 1
            try:
                segments['minutes'][index].changeValue(int(mins[index]))
            except:
                segments['minutes'][index].changeValue(None)
            try:
                segments['seconds'][index].changeValue(int(secs[index]))
            except:
                segments['seconds'][index].changeValue(None)
    else: for i in colon.children: i.opacity = 0
    time += 1; l.value = f'Overflow: {time>7200 and True or False} Colon: {time % 2 == 1} Time: {time/2-0.5}'
