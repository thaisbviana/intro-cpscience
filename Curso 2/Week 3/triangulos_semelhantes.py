class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        proporcao_1 = self.a/self.b == triangulo.a/triangulo.b
        proporcao_2 = self.b/self.c == triangulo.b/triangulo.c
        proporcao_3 = self.a/self.c == triangulo.a/triangulo.c
        
        if proporcao_1 == True and proporcao_2 == True and proporcao_3 ==True:
            return True
        else:
            return False
