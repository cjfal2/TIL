def ssavg(arr):
    return round((sum(arr)/len(arr)))

def mid(arr):
    return arr[int(len(arr)/2)]

def many(arr):
    counts = 0
    whatnum = []
    for i in arr :
        if counts < arr.count(i):
            counts = arr.count(i)
            whatnum.append(i)
    if len(whatnum) == 1 :
        return whatnum[0]
    else :
        return whatnum[1]

def minmax(arr):
    return max(arr)-min(arr)

def BS(a):    # a : 정렬할 List, N : 원소 수
    N = len(a)
    for i in range(N-1 , 0 , -1) :   # 범위의 끝 위치
        for j in range(0, i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1],a[j]
    return a

N = int(input())
L = []
for z in range(N):
    L.append(int(input()))
L = BS(L)

print(f'{ssavg(L):.0f}')
print(mid(L))
print(many(L))
print(minmax(L))