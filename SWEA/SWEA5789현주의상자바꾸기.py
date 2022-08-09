import sys
sys.stdin = open('boxch.txt','r')
#########
TC = int(input())

for tc in range(TC):
    N, Q = map(int,input().split()) 

    box = [0 for _ in range(N)] # N개의 0을 가진 리스트 생성 

    for i in range(1,Q+1):      # i번째 인풋을 받으면서 box리스트의 요소를 변경
        L, R = map(int,input().split())

        for k in range(L-1,R):  # 받은 입력 : 1을 0번째로 취급하기위해
            box[k] = i    # box리스트의 요소를 i 로 변경
    print(f'#{tc+1}',end=' ')   # 출력
    print(*box)   # 리스트를 가변인자로 주고 출력