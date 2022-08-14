import sys

while True:
    L=[]
    bal = sys.stdin.readline().rstrip()
    if bal == '.':
        break
    for i in bal:
        if i =='(' or i ==')' or i =='[' or i ==']':
            L.append(i)

    Q = ''.join(L)
    
    for i in range(len(Q)//2):
        Q = Q.replace('()', '')
        Q = Q.replace('[]', '')

    if len(Q) == 0:
        print('yes')
    else:
        print('no')