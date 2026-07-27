'''
3. Shape Area Calculator
Concepts: Inheritance basics + polymorphism
A Shape parent class with Circle, Rectangle, and Triangle subclasses, each overriding area().
Hints:
- Give Shape a method area() that just does 'pass' or raises NotImplementedError.
- Loop through a list of mixed shape objects and call .area() on each - notice you never check the type.
- This 'same method call, different behavior' is polymorphism - write a one-line note to yourself explaining why.
'''

class Shape:
    def area():
        raise NotImplementedError('Class most have area method')

class Rectangle(Shape):
    def __init__(self,length, height):
        self.length = length
        self.height = height
        

    # def area(self):
    #     return self.length * self.height
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



a = Rectangle(34,64)


# print(area)
    

        