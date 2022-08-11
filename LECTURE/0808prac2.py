import sys
sys.stdin = open('0808prac2.txt','r')

TC = int(input())
for tc in range(TC):
    arr = list(map(int,input().split()))
    N = len(arr)
    counts = 0
    for i in range(1<<N):
        M = []
        for j in range(N):
            if i&(1<<j):
                M.append(arr[j])
        if sum(M) == 0:
            counts += 1
            
    if counts == 1 :    #공집합은 모든 집합의 부분집합이므로 항상 sum(M) == 0 인 것이 하나는 있다.
        print(f'#{tc+1} 0')
    else :
        print(f'#{tc+1} 1')