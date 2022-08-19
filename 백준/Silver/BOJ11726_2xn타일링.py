N = int(input())
F = [0,1,2] + [0]*N
if N == 1 :
    print(1)
elif N == 2 :
    print(2)
else :
    for i in range(3,N+1) :
        F[i] = F[i-2] + F[i-1]
    if N < 10000:
        print(F[N])   
    else:
        print(F[N]%10007)