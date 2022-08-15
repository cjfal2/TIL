import sys
sys.stdin = open('ggh.txt','r')
#####################################
def mymax(arr):   #max 구현하기
    mymax1 = arr[0]   #첫번째 원소를 일단 가장 큰 수로 등록
    for i in arr:
        if mymax1 < i :
            mymax1 = i
    return mymax1   # 비교하면서 가장 큰 수 반환

def mymin(arr):  #min 구현하기
    mymin1 = arr[0]  #첫번째 원소를 일단 가장 작은 수로 등록
    for i in arr:
        if mymin1 > i :
            mymin1 = i   
    return mymin1   # 비교하면서 가장 작은 수 반환

#####
T = int(input())

for i in range(1,T+1):
    N , M = map(int,input().split())
    A = list(map(int,input().split()))

    L = []
    for k in range(len(A)-M+1) :
        MM = 0
        for m in range(M):
            MM += A[k+m] 
        L.append(MM)

    big = mymax(L)
    small = mymin(L)
    print(f'#{i} {big-small}')