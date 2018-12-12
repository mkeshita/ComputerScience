class Arrow:
    def __init__(self, x1, y1, x2, y2, **args):
        def checkSize(args):
            if ('size' in args):
                try:
                    return float(args['size'])
                except:
                    raise TypeError('size must be a float or int.')
            else:
                return 2
        self.checkSize = checkSize

        size = checkSize(args)
        self.x1 = x1; self.x2 = x2
        self.y1 = y1; self.y2 = y2
        self.arrow = Group(
            RegularPolygon(x2, y2, size+1, 3, rotateAngle = angleTo(x1, y1, x2, y2)),
            Line(x1, y1, x2, y2, lineWidth=size)
        )
# End Class

for i in range(0, 10):
    Arrow(
        randrange(0, 400),
        randrange(0, 400),
        randrange(0, 400),
        randrange(0, 400),
        size = randrange(1, 8)
    )
