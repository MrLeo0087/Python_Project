'''
3. Shape Area Calculator
Concepts: Inheritance basics + polymorphism
A Shape parent class with Circle, Rectangle, and Triangle subclasses, each overriding area().
Hints:
- Give Shape a method area() that just does 'pass' or raises NotImplementedError.
- Loop through a list of mixed shape objects and call .area() on each - notice you never check the type.
- This 'same method call, different behavior' is polymorphism - write a one-line note to yourself explaining why.
'''
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError('Class most have area method')

class Rectangle(Shape):
    def __init__(self,length, height):
        self.length = length
        self.height = height
        

    def area(self):
        return self.length * self.height
class Circle(Shape):
    def __init__(self,redius):
        self.redius = redius
        

    def area(self):
        return 3.14 * self.redius **2
    
class Triangle(Shape):
    def __init__(self,breath, height):
        self.breath = breath
        self.height = height
        

    def area(self):
        return 1/2*self.breath* self.height



# Create a mixed list of shape objects
shapes = [
    Rectangle(10, 5),
    Circle(7),
    Triangle(34, 64)
]

# Polymorphism: Calling .area() on each without checking its type!
for s in shapes:
    print(f"Area: {s.area()}")

# Note: Polymorphism lets different classes respond to the same method call (.area()) in their own specific way.
        