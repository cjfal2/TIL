import sys
input = sys.stdin.readline

L = int(input())
words = list(input())

abc = 'abcdefghijklmnopqrstuvwxyz'
qwert = {}
for idx , word in enumerate(abc,1):
    qwert[word] = idx
M = []
for m in words:
    M.append(qwert.get(m))
print(M)
M = M[:-1]
mysum = 0
for idx3 , num in enumerate(M) :
    mysum += num*(31**idx3)
print(mysum)