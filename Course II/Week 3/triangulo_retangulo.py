import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo (self):
        if self.a == math.sqrt(self.b**2 + self.c**2):
            return True
        elif self.b == math.sqrt(self.a**2 + self.c**2):
            return True
        elif self.c == math.sqrt(self.a**2 + self.b**2):
            return True
        else:
            return False