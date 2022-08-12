T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    print(f'#{i+1} {max(A)-min(A)}')