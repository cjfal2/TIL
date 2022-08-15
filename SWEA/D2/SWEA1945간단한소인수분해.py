T = int(input())

for tc in range(1,T+1):
    num = int(input())

    L = [2,3,5,7,11]
    counts = []
    for sosu in L:
        c = 0
        while True :
            if num%sosu == 0 :
                c += 1
                num = num//sosu
            else :
                counts.append(c)
                break
    J = ' '.join(map(str,counts))
    print(f'#{tc} {J}')