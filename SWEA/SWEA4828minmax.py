import sys
sys.stdin = open('minmax.txt','r')
##############
def mylen(arr1):
    counts = 0
    for _ in arr1:
        counts += 1
    return counts

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
    
    return mymin1  # 비교하면서 가장 작은 수 반환


###인풋###
T = int(input())

for tc in range(T):
    N = int(input())
    A = list(map(int,input().split()))
##########
    print(f'#{tc+1} {mymax(A)-mymin(A)}')  #f스트링을 이용해 특유의 테스트케이스 표시

