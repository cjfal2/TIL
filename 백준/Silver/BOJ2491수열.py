N = int(input())
A = list(map(int,input().split()))

count_p = 1
count_m = 1
L = [0]*N
if N == 1:
    print(len(A))
else :
    for i in range(1,N) :
        if A[i-1] < A[i] :
            count_p += 1
            count_m = 1
            L[i] = max([count_m,count_p])
        
        elif A[i-1] > A[i] :
            count_m += 1
            count_p = 1
            L[i] = max([count_m,count_p])
    
        else :
            count_m += 1
            count_p += 1
            L[i] = max([count_m,count_p])

    print(max(L))