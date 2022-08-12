import sys
sys.stdin = open('cards.txt','r')
#######################################
def mymax2(num1 , num2):   # 두 가지 수 중에 큰거 구하기
    if num1 > num2 :
        return num1     # 비교하면서 큰 수 반환
    else :
        return num2

def mycount(arr,target):  #리스트에서 원하는 숫자의 수 찾기
    counts = 0
    for i in arr:
        if i == target :
            counts += 1
    return counts

T = int(input())

for i in range(1,T+1):       #케이스넘버 출력이 편하게 1부터 범위 설정
    N = int(input())         
    cards = list(map(int,input()))     #map을 이용해 스트링으로 받은 문자열숫자를 각각 따로 int형으로 변환해서 리스트로 저장
    counts = 0     #카드의 수를 담는 변수
    whatnum = 0    #카드에 적힌 숫자를 담는 변수 
    for num in cards :       #cards의 요소를 불러옴
        if counts <= mycount(cards,num) :    #cards에서 해당 요소의 수를 세고, 미리 선언한 counts보다 크거나 같으면
            counts = mycount(cards,num)      #counts 변수에 요소의 수를 센 것을 저장한다.
            whatnum = mymax2(num,whatnum)     #혹시라도 카운트가 같을 수 있으니 whatnum과 새로운 num 중에 큰 것을 whatnum에 저장
    print(f'#{i} {whatnum} {counts}')      #f 스트링을 이용한 출력