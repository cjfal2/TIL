# 억지 스택
N = int(input())
L = []
for rc in range(N):
    R = list(input().split())
    for r in R :
        L.append(r)
    
    print(f'Case #{rc+1}:',end=' ')

    for _ in range(len(L)) :
        print(L.pop(),end = ' ')
    print()


# N = int(input())

# for rc in range(N):
#     L = list(input().split())[::-1]
#     print(f'Case #{rc+1}:',*L)