# 여기에 필요한 모듈을 추가합니다.
import json
import random

from pyparsing import line
class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        pass
        self.number_lines = []
    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        pass
        for i in range(n) :
            A = sorted(random.sample(range(1,46),6))
            self.number_lines.append(A)

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        pass
        DDate = self.get_draw_date(draw_number)
        print('==========================================')
        print(f'|             제 {draw_number} 회 로또            |')
        print('|                                        |')
        print(f'|        추첨일 : {DDate[0]}/{DDate[1]}/{DDate[2]} (토)        |')
        print('==========================================')
        for idx , k in enumerate(self.number_lines):
            if idx == 0 :
                j = 'A'
            elif idx == 1 :
                j = 'B'
            elif idx == 2 :
                j = 'C'
            elif idx == 3 :
                j = 'D'
            elif idx == 4 :
                j = 'E'
            print(f'     {j} : {k}      ')

    
    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        pass
        date1 = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        date2 = json.load(date1)
        date3 = date2.get('drwNoDate')
        year = date3[:4]
        month = date3[5:7]
        day = date3[8:]

        return (year, month, day)



    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        pass
        main_numbers = self.get_lotto_numbers(draw_number)[0]
        bonus_number = self.get_lotto_numbers(draw_number)[-1]
        print('==========================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('==========================================')
        abc = 'ABCDE'
        for idx , line in enumerate(self.number_lines):
            same_main_counts , is_bonus = self.get_same_info(main_numbers, bonus_number, line)
            rank = self.get_ranking(same_main_counts,is_bonus)
            if rank == 1 :    
                print(f'     {abc[idx]} : {same_main_counts}개 일치 (1등 당첨!)')
            elif rank == 2 :    
                print(f'     {abc[idx]} : {same_main_counts}개 일치 (2등 당첨!)')
            elif rank == 3 :    
                print(f'     {abc[idx]} : {same_main_counts}개 일치 (3등 당첨!)')
            elif rank == 4 :    
                print(f'     {abc[idx]} : {same_main_counts}개 일치 (4등 당첨!)')
            elif rank == 5 :    
                print(f'     {abc[idx]} : {same_main_counts}개 일치 (5등 당첨!)')
            elif rank == -1 :    
                print(f'     {abc[idx]} : {same_main_counts}개 일치 (낙첨)')
        print('==========================================')

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        pass
        numf = open(f'data/lotto_{draw_number}.json', encoding='utf-8')
        numg = json.load(numf)
        main_numbers = [0]*6
        for i in range(1,7):
            main_numbers[i-1] = numg.get(f'drwtNo{i}')
        bonus_number = numg.get('bnusNo')
        main_numbers.sort()
        
        return (main_numbers, bonus_number)
    
    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        pass
        is_bonus = False
        same_main_counts = 0
        for i in line:
            if i in main_numbers:
                same_main_counts += 1
        if bonus_number in line:
            is_bonus = True
        
        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        pass
        if same_main_counts == 6 :
            ranking = 1
        elif same_main_counts == 5 and is_bonus == True :
            ranking = 2
        elif same_main_counts == 5 :
            ranking = 3
        elif same_main_counts == 4 :
            ranking = 4
        elif same_main_counts == 3 :
            ranking = 5
        else :
            ranking = -1
        return ranking
