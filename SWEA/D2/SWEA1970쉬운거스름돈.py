'''
10
32850
160
562410
148950
1000000
16540
30
10
66660
999990
'''
money = [50000,10000,5000,1000,500,100,50,10]
for tc in range(int(input())):
    change = [0,0,0,0,0,0,0,0]
    N = int(input())
    for idx,m in enumerate(money):
        if N//m > 0:
            change[idx] += N//m
            N%=m
    print(f'#{tc+1}')
    print(*change)