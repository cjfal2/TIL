from collections import deque

for tc in range(int(input())):
    Q = deque()
    N, iwk = map(int,input().split())
    A = list(map(int,input().split()))

    for i in range(N):
        Q.append([i,A[i]])

    co = 1
    while True :
        maxnum = 0
        for j in Q :
            if j[1] > maxnum :
                maxnum = j[1]

        if Q[0][1] < maxnum :
            Q.append(Q.popleft())

        else :
            if Q[0][0] == iwk :
                print(co)
                break

            else :
                Q.popleft()
                co += 1