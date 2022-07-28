class Point:
    def __init__(self,x,y):
        self.x ,self.y = x, y

class Rectangle():
    def __init__(self,P1,P2):
        self.P1 = P1
        self.P2 = P2
        
    def get_area(self):
        pass
        return abs(self.P1.x-self.P2.x)*abs(self.P1.y-self.P2.y)

    def get_perimeter(self):
        pass
        return 2*(abs(self.P1.x-self.P2.x)+abs(self.P1.y-self.P2.y))

    def is_square(self):
        pass
        if abs(self.P1.x-self.P2.x)==abs(self.P1.y-self.P2.y):
            return True
        else :
            return False

p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3,7)
p4 = Point(6,4)
r2 = Rectangle(p3,p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
