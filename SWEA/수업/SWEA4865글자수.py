TC = int(input())

for tc in range(TC):
    A = input()
    B = list(' '.join(input().split()))
    L = 0
    for i in A:
        if L <= B.count(i) :
            L = B.count(i)
    
    print(f'#{tc+1} {L}')