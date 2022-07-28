class Doggy:
    # 클래스 변수 지정
    num_of_dogs = 0
    birth_of_dogs = 0
    # 생성자 함수
    def __init__(self,name,jong) -> None:
        self.name = name
        self.jong = jong
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self):
        return 'bow!wow!'
    # 개가 죽는 경우
    def __del__(self):
        Doggy.num_of_dogs -= 1
    # 클래스 함수
    @classmethod #클래스 메서드라고 데코레이터 지정
    def get_status(cls):
        return f'Birth : {cls.birth_of_dogs}, Current count: {cls.num_of_dogs}'
    

# @classmethod가 있으면 Doggy.get_status()에 괄호가 비어있어야 하고
# 없으면 ()안에 dog1을넣어줘야 되네요

dog1 = Doggy('뽀삐','진돗개')
print(dog1.get_status())   # Birth : 1, Current count: 1
print(dog1.bark())     # bow!wow!
dog2 = Doggy('초코','풍산개')
print(dog1.get_status())   # Birth : 2, Current count: 2
print(dog2.get_status())    # Birth : 2, Current count: 2
print(dog2.bark())    # bow!wow! 
del dog2    #dog2 삭제
print(dog1.get_status())    #   Birth : 2, Current count: 1
# print(dog2.bark())   : 에러
