N = int(input())
info = []
for _ in range(N):
    x , y = list(map(str,input().split()))
    A = [int(x),y]
    info.append(A)

info.sort(key=lambda x:x[0])

for i in info :
    print(*i)