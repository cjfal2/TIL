N = int(input())

if N == 1:
    print(1)
else:
    NN = N//2
    if NN == 2:
        print(2)
    else:
        L=0
        R=NN
        while L<=R:
            mid=(L+R)//2
            if mid*mid == N:
                print(mid)
                break
            elif mid*mid < N:
                L = mid+1
            else:
                R = mid-1