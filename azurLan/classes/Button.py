class Btn:
    def __init__(self, x, y, r, g, b):
        self.x = x
        self.y = y
        self.color = Color(r, g, b)

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
