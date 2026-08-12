class Circle:
    def __init__(self, radius):
        self.radius =  radius

    def area(self):
        self.area = 3.14* self.radius**2
        return self.area
    def  parameter(self):
        self.parameter = 2*3.14*self.radius
        return self.parameter
c1 = Circle(21)
print("The area of the circle is :", c1.area())
print("The parameter of the circle is :", c1.parameter())