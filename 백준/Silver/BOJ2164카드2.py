from collections import deque

Q = deque()
N = int(input())
for i in range(1, N + 1):
    Q.append(i)

if Q == [1]:
    print(1)
else:
    while len(Q) != 1 :
        Q.remove(Q[0])
        Q.append(Q.popleft())
    print(Q[0])
    