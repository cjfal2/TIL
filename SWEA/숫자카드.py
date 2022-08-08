#0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
#가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
#
#[입력]
#첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
#다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
#다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 
#
#[출력]
#각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.
#######################################

T = int(input())

for i in range(1,T+1):       #케이스넘버 출력이 편하게 1부터 범위 설정
    N = int(input())         
    cards = list(map(int,input()))     #map을 이용해 스트링으로 받은 문자열숫자를 각각 따로 int형으로 변환해서 리스트로 저장
    counts = 0     #카드의 수를 담는 변수
    whatnum = 0    #카드에 적힌 숫자를 담는 변수 
    for num in cards :       #cards의 요소를 불러옴
        if counts <= cards.count(num) :    #cards에서 해당 요소의 수를 세고, 미리 선언한 counts보다 크거나 같으면
            counts = cards.count(num)      #counts 변수에 요소의 수를 센 것을 저장한다.
            whatnum = max(num,whatnum)     #혹시라도 카운트가 같을 수 있으니 whatnum과 새로운 num 중에 큰 것을 whatnum에 저장
    print(f'#{i} {whatnum} {counts}')      #f 스트링을 이용한 출력