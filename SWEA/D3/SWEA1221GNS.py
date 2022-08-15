import sys
sys.stdin = open('sample.txt','r')

TC = int(input())
for tc1 in range(TC):
    tc , N = input().split()
    text = input()
    N = int(N)
    target = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    L = []
    for strnum in target :
        i = -4

        for _ in range(N):
            i += 4
            if text[i:i+3] == strnum :
                L.append(strnum)
    print(tc)
    print(*L)