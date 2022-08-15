import sys
sys.stdin = open('oneone.txt','r')
############
TC = int(input())

for tc in range(TC):
    N = int(input())
    onez = input()+'0'
    counts = 0
    c = []
    for i in range(N+1):
        if onez[i] == '1':
            counts += 1
        else :
            c.append(counts)
            counts=0
    print(f'#{tc+1} {max(c)}')
