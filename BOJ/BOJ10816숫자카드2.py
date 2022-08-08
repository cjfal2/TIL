import sys
sys.stdin = open('BOJ10816숫자카드2.txt','r')

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



N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

A = Counting_Sort(A)

for i in B :
    if i == B[-1] :
        print(binary(A,i))
    else :
        print(binary(A,i),end=' ')
