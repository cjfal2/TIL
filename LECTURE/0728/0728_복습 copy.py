class Nationality:
    def __init__(self,nation):
        self.nation = nation
        
    def __str__(self) -> str:
        return f'나의 국적은 {self.nation}'

    def nation1(self):
        print(f'나의 국적은 {self.nation}')


korea_nationality = Nationality("대한민국")
korea_nationality.nation1() # 나의 국적은 대한민국
print(korea_nationality)

