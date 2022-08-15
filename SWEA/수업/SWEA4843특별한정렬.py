##################################

def CS(A) : 
# k : A 의 가장 큰 수
    k = mymax(A)
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

def mymax(arr1):
    mymy = 0
    for i in arr1:
        if i >= mymy :
            mymy = i
    return mymy

TC = int(input())

for tc in range(TC):
    N = int(input())
    arr = list(map(int,input().split()))
    CS_arr = CS(arr)
    CS_f = CS_arr[:5]
    CS_b = CS_arr[-1:-6:-1]
    L = [0]*10
    for i in range(0,10,2):
        L[i] = CS_b[i//2]
        L[i+1] = CS_f[i//2]
    print(f'#{tc+1}',end=' ')
    for i in range(10) :
        if i == 9 : 
            print(L[i])
        else :
            print(L[i],end=' ')