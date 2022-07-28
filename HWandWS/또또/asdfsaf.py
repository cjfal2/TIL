class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def check_age(self):
        if self.age > 19 :
            return False
        else :
            return True

A = Person('jhon',26)
B = Person('jein',16)

print(A.check_age())
print(B.check_age())