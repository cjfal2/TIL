import sys
sys.stdin = open('sample.txt','r')

for TC in range(10):
    long , text = input().split()
    text = list(text)
    L = []
    while True :
        if len(text) > 0:
            L.append(text[0])
            text.pop(0)

        if len(L) > 1 :
            if L[-2] == L[-1]:
                L.pop()
                L.pop()

        if len(text) == 0:
            break

    print(f'#{TC+1}',end=' ')
    print(*L,sep='')