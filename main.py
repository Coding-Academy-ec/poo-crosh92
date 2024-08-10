class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo:
    pi = 3.141592653589793

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.pi * (self.radio ** 2)
    