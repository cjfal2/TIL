class Animal:
    def __init__(self,name):
        self.name = name
    
    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):
    def run(self):
        print(f'{self.name}! 달린다!')
    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def fly(self):
        print(f'{self.name}! 푸드덕!')
    
dog = Dog('꼽이')
dog.run()     #꼽이! 달린다!
dog.bark()    #꼽이! 짖는다!

bird = Bird('구구')
bird.walk()    #구구! 걷는다!
bird.eat()     #구구! 먹는다!
bird.fly()     #구구! 푸드덕!