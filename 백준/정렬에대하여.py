def BubbleSort1(arr):    # a : 정렬할 List, N : 원소 수
    a = arr[:]
    N = len(a)
    for i in range(N-1 , 0 , -1) :   # 범위의 끝 위치
        for j in range(0, i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1],a[j]
    return a

def BubbleSort2(arr):    # a : 정렬할 List, N : 원소 수
    a = arr[:]
    N = len(a)
    for i in range(N-1) :   
        for j in range(N-1,i,-1) : # 범위의 끝 위치
            if a[j -1] > a[j] :
                a[j-1], a[j] = a[j],a[j-1]
    return a

# 음수는 처리하지 못함
def Counting_Sort(A) : # A : 정렬할 리스트
    k = max(A)
    Brr = [0] * len(A)  # 정렬될 배열
    C = [0] * (k+1)  # temp 생성

    for i in range(0,len(A)):  #수 세기
        C[A[i]] += 1
    
    for i in range(1,len(C)):   #누적 과정
        C[i] += C[i-1]
    
    for i in range(len(Brr)-1,-1,-1):
        C[A[i]] -= 1
        Brr[C[A[i]]] = A[i]

    return Brr

def selsort(arr):
    A = arr[:]
    N = len(A)
    for i in range(N-1):
        minidx = i
        for j in range(i+1,N):
            if A[minidx] > A[j]:
                minidx = j
        A[minidx] , A[i] = A[i] , A[minidx]
    return A

L = list(map(int,input().split()))
X1 = BubbleSort1(L)
X2 = BubbleSort2(L)
Y = Counting_Sort(L)
Z = selsort(L)

print(X1, 'buble1')
print(X2, 'buble2')
print(Y, 'count')
print(Z, 'sel')