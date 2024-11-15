from math import sqrt

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            sign = '+'
        else:
            sign = '-'
        return f"{self.real}{sign}{self.imaginary}i"

    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __eq__(self, other):
        return ComplexNumber(self.real == other.real, self.imaginary == other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        real = self.real * other.real + self.imaginary * other.imaginary / other.real**2 + other.imaginary**2
        imaginary = self.real * other.imaginary - self.imaginary * other.real / other.real**2 + other.imaginary**2
        return ComplexNumber(real, imaginary)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)


