def money(want):
    co = []
    for i in coins :
        if i <= want :
            co.append(i)
    return co

N,K = map(int,input().split())

coins = [int(input()) for _ in range(N)]

need_coin = money(K)[::-1]

nc = 0
for i in need_coin:
    nc += K//i
    K = K%i
    if K == 0 :
        break

print(nc)