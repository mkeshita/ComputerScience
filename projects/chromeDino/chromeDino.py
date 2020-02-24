import math
# Colors
app.colors = {
    "blurple": rgb(114, 137, 218),
    "fullWhite": rgb(255, 255, 255),
    "greyple": rgb(153, 170, 181),
    "darkNotBlack": rgb(44, 47, 51),
    "notQuiteBlack": rgb(35, 39, 42)
}
########## START SETTINGS ##########
app.color = app.colors['blurple']; app.background = app.colors['notQuiteBlack']
app.steps = 0; app.stepsPerSecond = 60 # Don't change this value! | Clock
app.ground = Line(0, 300, 400, 300, fill=app.color) # Ground
app.dino = Rect(50, 0, 20, 50, fill=app.color) # Dino
app.dino.bottom = app.ground.top # Move Dino to floor.
app.dinoJumping = False; app.dinoJumpVal = 0 # Jumping Clock
app.score = Label( # Score Label
    0, app.right-60, app.top+25,
    fill=app.colors['greyple'],
    font='monospace', size=32, bold=True
)
########## END SETTINGS ##########

# Generate Cactus
activeCacti = []
def cacti():
    bL = 15
    g = Group(
        Line(200, 240, 200, 300, lineWidth=10), # Body
        Line(200-bL, 280, 200, 280, lineWidth=6), # Left Branch
        Line(200-bL, 280, 200-bL, 260, lineWidth=6),
        Line(200+bL, 270, 200, 270, lineWidth=6), # Right Branch
        Line(200+bL, 270, 200+bL, 250, lineWidth=6),
    )
    for i in g.children: i.fill = app.color
    activeCacti.extend(g)
    return g

def onKeyHold(k): # Jump System
    if (('w' in k) or ('up' in k) or ('space' in k)): app.dinoJumping = True

def onStep():
    app.steps += 1 # Increase Steps
    if (app.steps % 8 == 0): app.score.value += 1 # Increase Score

    # Cactus Generation
    cloc = 600
    if (randrange(cloc) == rounded(cloc / 2)): # Cacti Movement System
        c = cacti()
        c.centerX = 420
    for i in activeCacti:
        i.centerX -= 2

    if (app.dinoJumping == True): # Dino Jump
        app.dino.bottom = math.cos((app.dinoJumpVal*-3)/app.stepsPerSecond)*60+240
        app.dinoJumpVal += 1
    if (app.dinoJumpVal > 10): # Floor Hit Detection
        if (app.dino.hitsShape(app.ground)):
            app.dinoJumping = False
            app.dinoJumpVal = 0

    # Cacti Hit Detection
    for i in activeCacti:
        if (app.dino.hitsShape(i)):
            app.stop()
