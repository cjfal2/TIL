import sys
input = sys.stdin.readline

def ssavg(arr):
    return round((sum(arr)/len(arr)))

def mid(arr):
    return arr[int(len(arr)/2)]

def many(arr):
    dic = {}
    for i in arr :
        if i not in dic :
            dic[i] = 1
        else :
            dic[i] = dic[i] + 1
    B = max(dic.values())
    A = list(dic.items())
    A.sort(key=lambda x:x[1],reverse=True)
    
    C = []
    for j in A:
        if j[1] == B:
            C.append(j)
    if len(C) == 1 :
        return A[0][0]
    else :
        return A[1][0]

def minmax(arr):
    return max(arr)-min(arr)

N = int(input().strip())
L = []
for _ in range(N):
    L.append(int(input().strip()))
L.sort()

print(f'{ssavg(L):.0f}')
print(mid(L))
print(many(L))
print(minmax(L))