# 2. Create abstract base class "shape" that has abstract method "area". Inherit rectangle, triangle
# and square class from shape class and provide implementation of "area" method for each
# derived class. Finally print area of rectangle, triangle and square. [2 marks]


from abc import ABC,abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def __init__(self, width ,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class square(shape):
    def __init__(self,height):
        self.height = height

    def area(self):
        return self.height * self.height

r = Rectangle(4,5)
t = triangle(3,4)
s = square(4)
print(f"area of rectangle {r.area()}")
print(f"area of triangle {t.area()}")
print(f"area of square {s.area()}")

