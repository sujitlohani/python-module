"""Create a base class called Shape that has a method named calculateArea(). This method should return 0 as a default value, indicating the area of a shape.

Create two derived classes:

Circle, which overrides the calculateArea() method to calculate and return the area of a circle. The formula for the area of a circle is:

Area = 𝜋 × radius^2

Rectangle, which overrides the calculateArea() method to calculate and return the area of a rectangle. The formula for the area of a rectangle is:

Area = length * width

In the main method (or driver code), do the following:

Create objects of type Circle and Rectangle with appropriate dimensions (e.g., radius for the circle, length and width for the rectangle).

Call the calculateArea() method on these objects and display the calculated areas."""

class Shape:
    def calculate_Area():
        return 0
    
class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_Area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle (Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_Area(self):
        return self.length * self.breadth
    

def main():
    circle = Circle (5)
    rectangle = Rectangle (10, 5)

    print (f"Area of circle: {circle.calculate_Area()}")
    print (f"Area of rectangle: {rectangle.calculate_Area()}")

main()

