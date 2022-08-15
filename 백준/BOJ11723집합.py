import sys
# input = sys.stdin.readline
sys.stdin = open('sample.txt','r')

N = int(input().strip())

S = set([])
for _ in range(N):
    K = input().strip().split()

    if K[0] == 'all' :
        S = {str(i) for i in range(1,21)}
    if K[0] == 'add' :
        S.add(K[1])
    if K[0] == 'remove' :
        S.discard(K[1])
    if K[0] == 'check' :
        if K[1] in S :
            print(1)
        else :
            print(0)
    if K[0] == 'toggle' :
        if K[1] in S:
            S.discard(K[1])
        else :
            S.add(K[1])
    if K[0] == 'empty' :
        S = set([])