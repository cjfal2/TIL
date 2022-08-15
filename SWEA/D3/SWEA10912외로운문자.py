TC = int(input())
for tc in range(TC):
    A = sorted(input())
    L = []
    for a in A :
        if a not in L :
            L.append(a)
        elif a in L :
            L.remove(a)
    if L == [] :
        print(f'#{tc+1} Good')
    else :
        L = ''.join(map(str,L))
        print(f'#{tc+1} {L}')