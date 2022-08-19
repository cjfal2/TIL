import sys
input = sys.stdin.readline

def vi(arr,target):
    s = 0
    e = len(arr)-1
    global c
    while s <= e :
        m = (s+e)//2
        if arr[m] == target:
            c += 1
            break
        elif arr[m] > target:
            e = m-1
        else :
            s = m+1
while 1:
    N , M = map(int,input().strip().split())
    if N == 0 and M == 0:
        break

    SG = []
    for _ in range(N):
        SG.append(int(input().strip()))

    SY = []
    for _ in range(M):
        SY.append(int(input().strip()))

    c = 0
    for i in SY:
        vi(SG,i)
    print(c)