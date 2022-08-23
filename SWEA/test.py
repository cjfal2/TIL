# import sys
# sys.stdin = open('sample.txt','r')

for TC in range(10):
    tc = int(input())
    target = input()
    text = input()

    N = len(text)
    M = len(target)

    i = -1
    
    counts = 0
    while i != N:
        i += 1
        if text[i:i+M] == target :
            counts += 1
    print(f'#{tc} {counts}')