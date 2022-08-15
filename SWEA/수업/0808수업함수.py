def BubbleSort(a , N):    # 정렬할 List, N 원소 수
    for i in range(N-1 , 0 , -1) :   # 범위의 끝 위치
        for j in range(0, i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1],a[j]
    return a

def Counting_Sort(A,k) : 
# k : A 의 가장 큰 수
    
    B = [0] * len(A)  # 정렬될 배열
    C = [0] * (k+1)  # temp 생성

    for i in range(0,len(A)):  #수 세기
        C[A[i]] += 1
    
    for i in range(1,len(C)):   #누적 과정
        C[i] += C[i-1]
    
    for i in range(len(B)-1,-1,-1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    
    return B