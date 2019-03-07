app.stepsPerSecond = 60
s = 5; d = Circle(200, 200, 25, fill='purple')

def onKeyHold(keys):
    # Movement Control
    if ('right' in keys): d.centerX += s
    if ('left' in keys): d.centerX -= s
    if ('up' in keys): d.centerY -= s
    if ('down' in keys): d.centerY += s

    # Edge Movement
    if (d.left >= app.right): d.right = app.left
    elif (d.right <= app.left): d.left = app.right
    if (d.top >= app.bottom): d.bottom = app.top
    elif (d.bottom <= app.top): d.top = app.bottom
