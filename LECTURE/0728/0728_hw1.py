class Circle:
    pi = 3.14

    def __init__(self,r,x,y):
        self.r =r
        self.x =x
        self.y =y

    def area(self):
        return Circle.pi*self.r*self.r

    def circumference(self):
        return 2*Circle.pi*self.r

    def center(self):
        return (self.x, self.y)

myO = Circle(3,2,4)
print(myO.circumference())
print(myO.area())