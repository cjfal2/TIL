import sys
input = sys.stdin.readline

def push(arr,st):
    a = arr[:]
    a.append(st)
    if len(a) < 2 :
        return a
    else :
        if a[-2] == '(' and a[-1] == ')' :
            a.pop()
            a.pop()
            return a
        else :
            return a

for _ in range(int(input().strip())):
    L = list(input().strip())
    Q = []
    for i in L:
        Q = push(Q,i)
    if len(Q) == 0 and L != [] :
        print('YES')
    else :
        print('NO')