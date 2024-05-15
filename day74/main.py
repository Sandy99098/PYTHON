# Your Python code goes here
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)  # Initialize the base class with the same radius for x and y

    def area(self):
        return 3.14 * self.radius * self.radius  # Correct area calculation for a circle

s = Shape(1, 3)
c = Circle(7)
print(s.area())  

print(c.area())  

