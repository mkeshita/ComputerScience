### Instructions! ###
# Used and modified my previous creative task because I ran out of time and
# wasn't here on Friday.
#
# Changes from the previous creative task are as listed >>
# - Run the application more than once, the bumper color is selected generated.
# - `onMouseMove` & `onMouseDrag` both are linked to the same function, `init`.
# - A lot of things run longer than 80 characters to compact untouched code, so
#   expect a lot of it to not look very pretty.
# - The limiter at the bottom uses a sudo if statement to also compact long code.
# - Because pylint doens't allow global variables you may have to run this code
#   in the sandbox unfortunately. The global variable is required to make the
#   code efficient.
### Instructions! ###

### Init
app.background = 'beige'; app.stepsPerSecond = 7.5
metalColor = 'slateGrey'; bumperColor = choice(['blue', 'red'])
Rect(365, 370, 30, 30, fill='gold') # Power Cube

### Functions
def genBumper(x, y, color): return Group(Rect(x, y, 30, 15, fill=color), Label('4150', x+15, y+7, fill='white', bold=True))
def genWheel(x): return Circle(x, 390, 10, border='white')
def genArm(x): return Line(x, 385, x, 285, lineWidth=5, fill=metalColor)

### Build Robot
# Chassis
robot = Group(
    genWheel(75), genWheel(100), genWheel(125),
    Rect(50, 385, 100, 10, fill=metalColor),
    Line(125, 286, 57, 388, lineWidth=5, fill=metalColor),
    Rect(120, 350, 5, 5), # 5
    Circle(120, 352.5, 2.5) # 6
)

# Arms
arm0 = genArm(125); arm1 = genArm(130); arm2 = genArm(135)
arm3 = Line(140, 385, 140, 345, lineWidth=5, fill=metalColor)
arm4 = Line(140, 382, 180, 382, lineWidth=3.5) # Grabber
arm = Group()
for i in range(0, 5): arm.add(eval(f'arm{i}'))

# Bumpers
bumper = Group(genBumper(120, 382.5, bumperColor), genBumper(50, 382.5, bumperColor))

# Running Light
statusLight = 'orange'
def onStep():
    global statusLight
    if (statusLight == 'yellow'): statusLight = 'darkRed'
    else: statusLight = 'yellow'
    robot.children[5].fill = statusLight; robot.children[6].fill = statusLight

### Movement
def onMouseMove(x, y): init(x, y)
def onMouseDrag(x, y): init(x, y)
def init(x, y):
    # Limiter
    x = {x < 105: 105, x > 365: 365}.get(True, x) # Sudo if statement on one line.
    y = {y < 140: 140, y > 385: 385}.get(True, y)
    robot.left = x - 100; arm.left = x - 25; bumper.left = x - 100
    arm1.y1 = (y / 3) + 157; arm1.y2 = (y / 3) + 257
    arm2.y1 = (y / 1.5) + 28; arm2.y2 = (y / 1.5) + 128
    arm3.y1 = y; arm3.y2 = y - 40; arm4.y1 = y - 3; arm4.y2 = y - 3
