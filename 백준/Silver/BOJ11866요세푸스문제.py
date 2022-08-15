N , K = map(int,input().split())

from collections import deque

Q = deque()

for i in range(1, N + 1):
    Q.append(i)

L = []
i = 0
while len(L) < N :
    i+=1
    if i%K == 0 :
        L.append(Q.popleft())
    else :
        a = Q.popleft()
        Q.append(a)
print('<',end='')
print(*L,sep=', ',end='')
print('>')