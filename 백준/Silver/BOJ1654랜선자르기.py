def cut(mid):
    co = 0
    for i in lan:
        if i >= mid :
            co += i//mid
    return co >= want

K,want = map(int,input().split())
lan = sorted([int(input()) for _ in range(K)])

L = 1  #????? 왜 0 아니고 1로 하면 맞지
R = lan[-1]
while L <= R :
    mid = (L+R)//2
    if cut(mid):
        L = mid + 1
    else :
        R = mid - 1
print(R)