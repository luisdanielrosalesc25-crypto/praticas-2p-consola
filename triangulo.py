class triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2
     
    def perimetro(self):
        return self.base + self.altura + self.altura