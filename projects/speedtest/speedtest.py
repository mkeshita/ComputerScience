import math

### START SETTINGS ###
app.colors = {
    'appBackground': rgb(20, 21, 38),
    'speedBackground': rgb(35, 47, 78),
    'downloadSpeed': rgb(102, 204, 255),
    'uploadSpeed': rgb(75, 75, 255)
}

app.background = app.colors['appBackground']
app.stepsPerSecond = 60
app.steps = 0

seed(17754977)  # Debugging Seed

app.memory = {  # I don't recommend touching any of this.
    'stage': 0,
    'downloadMax': randrange(25, 300), 'testDSClock': 0, 'dSpeedLimit': 0,
    'uploadMax': randrange(12, 120), 'testUSClock': 0, 'uSpeedLimit': 0
}
### END SETTINGS ###

### Speed Test Indicator
speedTest = Group(
    Arc(200, 200, 300, 300, -135, 0.1, fill=app.colors['speedBackground']),
    Arc(200, 200, 300, 300, -135, 0.1, fill=app.colors['downloadSpeed']),
    Circle(200, 200, 300 / 2 - 37.5, fill=app.colors['appBackground']),
    Label('Connecting', 200, 300, fill='white', size=22, bold=True),
    Label(0, 200, 325, fill='white', size=2*18, bold=True),
    Label('Mbps', 200, 345, fill='white', size=12, bold=True)
)
speedTest.opacity = 0

### Press Go!
go = Group(
    Circle(
        200, 200, 75,
        fill=app.colors['appBackground'], border=gradient(
            app.colors['uploadSpeed'], app.colors['downloadSpeed'], start='bottom'
        )
    ),
    Label('GO', 200, 200, fill='white', size=2*18, bold=True)
)


def testSpeed(clock, max):
    app.memory[clock] += 1
    rawVal = (app.memory[clock] * 0.80) + randrange(-5, 5)
    roundedVal = rounded(rawVal * 0.37 + 0.1)
    sweep = rawVal
    if (sweep <= 0):
        sweep = 1
    elif (sweep >= 270):
        sweep = 270
    speedTest.children[1].sweepAngle = sweep
    if (app.memory[clock] % 10 == 0):
        speedTest.children[4].value = roundedVal
    if (roundedVal >= app.memory[max]):
        app.memory['stage'] += 1


def speedLimit(oldClock, newClock, max):
    app.memory[newClock] += 1
    rawVal = (app.memory[oldClock] * 0.80) + randrange(-5, 5)
    roundedVal = rounded(rawVal * 0.37 + 0.1)
    sweep = rawVal
    if not (rawVal >= 270):
        speedTest.children[1].sweepAngle = rawVal
    else:
        speedTest.children[1].sweepAngle = 270
    if (app.memory[newClock] % 10 == 0):
        speedTest.children[4].value = roundedVal
    if (app.memory[newClock] == 60*4.5):
        app.memory['stage'] += 1


def resetTest():
    if not (speedTest.children[1].sweepAngle - 2 <= 2):
        speedTest.children[1].sweepAngle -= 2
    else:
        speedTest.children[1].sweepAngle = 0.1
        app.memory['stage'] += 1


def labelRotate(string, clock):
    if (app.memory[clock] % 20 == 0):
        b = speedTest.children[3]
        if (b.value == f'{string}.'):
            b.value = f'{string}..'
        elif (b.value == f'{string}..'):
            b.value = f'{string}...'
        elif (b.value == f'{string}...'):
            b.value = f'{string}.'
        else:
            b.value = f'{string}.'

### onMouseMove


def onMouseMove(x, y):
    s = go.children[0]
    if (go.contains(x, y)):
        s.fill = app.colors['speedBackground']
    else:
        s.fill = app.colors['appBackground']

### onMousePress


def onMousePress(x, y):
    if ((app.memory['stage'] == 0) and (go.contains(x, y))):
        app.memory['stage'] += 1

### onStep


def onStep():
    app.steps += 1
    ### Start Animations
    if (app.memory['stage'] == 1):
        if (go.opacity - 1.5 >= 0):
            go.opacity -= 1.5
            speedTest.opacity += 1.5
            speedTest.children[0].sweepAngle += 4.1
        else:
            go.visible = False
            app.memory['stage'] += 1
            speedTest.children[0].sweepAngle = 270
    ### Test Download Speed
    elif (app.memory['stage'] == 2):
        testSpeed('testDSClock', 'downloadMax')
        labelRotate('Downloading', 'testDSClock')
    elif (app.memory['stage'] == 3):
        speedLimit('testDSClock', 'dSpeedLimit', 'downloadMax')
        labelRotate('Downloading', 'dSpeedLimit')
    elif (app.memory['stage'] == 4):
        resetTest()
        speedTest.children[3].value = 'Download Speed:'
        app.memory['dFinal'] = speedTest.children[4].value
    ### Test Upload Speed
    elif (app.memory['stage'] == 5):
        speedTest.children[1].fill = app.colors['uploadSpeed']
        testSpeed('testUSClock', 'uploadMax')
        labelRotate('Uploading', 'testUSClock')
    elif (app.memory['stage'] == 6):
        speedLimit('testUSClock', 'uSpeedLimit', 'uploadMax')
        labelRotate('Uploading', 'uSpeedLimit')
    elif (app.memory['stage'] == 7):
        resetTest()
        speedTest.children[3].value = 'Upload Speed:'
        app.memory['uFinal'] = speedTest.children[4].value
    ### Ending Animations
    elif (app.memory['stage'] == 8):
        app.memory['stage'] += 1
        for i in range(3, 6):
            speedTest.children[i].value = ''
        app.memory['results'] = Group(
            Label('Download', 150, 200, fill='white', size=18),
            Label(app.memory['dFinal'], 150, 220, fill='white', size=18),
            Label('Upload', 250, 200, fill='white', size=18),
            Label(app.memory['uFinal'], 250, 220, fill='white', size=18)
        )
        app.memory['results'].opacity = 0
    elif (app.memory['stage'] == 9):
        if (app.memory['results'].opacity + 2.5 >= 100):
            app.memory['stage'] += 1
        else:
            app.memory['results'].opacity += 2.5
