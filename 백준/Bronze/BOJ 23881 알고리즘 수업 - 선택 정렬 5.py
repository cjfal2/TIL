def SUM(arr):
    co = 0
    for i in arr:
        co += i
    return co

def LEN(arr):
    co = 0
    for _ in arr:
        co += 1
    return co

def SC(arr):
    N = LEN(arr)
    if arr == B:
            return 1
    for i in range(N-1,0,-1):
        MAX = i
        for j in range(i-1,-1,-1):
            if arr[j] > arr[MAX]:  
                MAX = j
        arr[i],arr[MAX]=arr[MAX],arr[i]
        if arr == B:
            return 1
    return 0

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(SC(A))