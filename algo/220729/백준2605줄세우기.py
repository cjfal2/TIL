N = int(input())

L = list(map(int,input().split()))

M = [1]

for idx, card in enumerate(L[1:]):
    M.insert(card,idx+2)

print(*M[::-1])
