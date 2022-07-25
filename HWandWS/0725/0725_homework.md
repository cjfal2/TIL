# 1. 모음은 몇 개나 있을까?
- 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를
작성하시오. .count() 메서드를 활용하여 작성하시오.
```python
def count_vowels(word):
    moum = 'aeiou'
    moum_num = 0
    for i in word:
        if i in moum:
            moum_num += 1
    return moum_num

print(count_vowels('apple'))  #2
print(count_vowels('banana'))  #3
```
# 2. 문자열 조작
(4)  .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다. -> 공백(스페이스)을 제거

# 3. 정사각형만 만들기
- 각각 너비와 높이의 값으로 이루어진 2개의 list를 전달 받아, 각각의 값들을 조합하여 만들 수 있는 정사각형만의 넓이를 담은 list를 반환하는 only_square_area 함수를 작성하시오.
```python
def only_square_area(A_list,B_list):
    sq = []
    for num_A in A_list:
        if num_A in B_list:
            sq.append(num_A)
    new_sq = []
    for n in sq:
        new_sq.append(n**2)
    return new_sq
        
print(only_square_area([32, 55, 63], [13, 32, 40, 55]))  # => [1024, 3025]
```