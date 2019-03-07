### Instructions/Information
# I spent most of my time on functionality and refining little things.
# Controls:
#  - W accelerates the vehicle forward.
#  - S decelerates the vehicle and can also switch it into reverse.
#  - A rotates the front tires left to turn the vehicle in that direction.
#  - D rotates the front tires right to turn the vehicle in that direction.
#  - Tip: You can hold down each key so you don't have to press it a gazillion
#    times to get the same effect.

### Setup the step system.
app.stepsPerSecond = 60; app.steps = 0

### Colors | Because this is easier to manage everything in one place.
app.background = 'lightSlateGray'
colors = {'vehicle': 'fireBrick', 'windows': 'skyBlue'}

### Hud at the top.
def h(i): return Label('', app.centerX, app.top+i)
hud = Group(h(15), h(5))

### All the predefined functions for the vehicle shapes.
# Was going to add headlights but do to some complications I decided not to add
# it. I kept the function just incase I decide to add it in the future.
def Lit(x): return Arc(200+x, 200, 50, 150, -45, 90, fill=colors['headlights'], opacity=50)
def Bump(y): return Oval(200, 200+y, 25, 5, fill=colors['vehicle'])
def Tire(x, y): return Line(200+x, 200+y, 200+x, 210+y, lineWidth=3)
def Win(y, a):
    return Polygon(
        200-5, 200+y, 200+5, 200+y,
        200+10, 210+y, 200-10, 210+y,
        fill=colors['windows'],
        rotateAngle=a
    )

### The actual vehicle itself.
v = Group(
    Line(200, 200, 200, 250, lineWidth=25, fill=colors['vehicle']), # Body
    Bump(0), Bump(50), # Bumpers
    Tire(-12, 5), Tire(12, 5), Tire(-12, 35), Tire(12, 35), # Tires
    Win(5, 180), Win(35, 0) # Windows
); v.ds = 0; v.dd = 0

### Speed and Movement event.
def onKeyHold(k):
    if (app.steps % 10 == 0):
        if (('w' in k) and (v.ds < 10)): v.ds += 1
        if (('s' in k) and (v.ds > -5)): v.ds -= 1
        if (('a' in k) and (v.dd > -8)): v.dd -= 1
        if (('d' in k) and (v.dd < 8)): v.dd += 1

### Literally *everything* that makes *everything* work for the most part.
def onStep():
    app.steps += 1

    # Vehicle Movement
    v.dx = (0.005 * v.ds) * (v.x1 - v.x2)
    v.dy = (0.005 * v.ds) * (v.y1 - v.y2)
    v.centerX += v.dx; v.centerY += v.dy

    # Vehicle Rotation
    if (v.rotateAngle >= 360): v.rotateAngle = 0
    if (v.rotateAngle <= -1): v.rotateAngle = 359
    v.rotateAngle += (0.5 * v.dd) * (v.ds * 0.1)

    # Tire Rotation on Vehicle
    for i in range(3, 5): v.children[i].rotateAngle = v.dd * 5 + v.rotateAngle

    # Loop the vehicle to the other side of the "map."
    if (v.left >= app.right): v.right = app.left
    elif (v.right <= app.left): v.left = app.right
    if (v.top >= app.bottom): v.bottom = app.top
    elif (v.bottom <= app.top): v.top = app.bottom

    # Hud Event
    hud.children[0].value = f'Speed: {v.ds}'
    hud.children[1].value = f'Direction: {v.dd}'
