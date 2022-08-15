import sys

n,k = map(int,sys.stdin.readline().split())
r = n-k
def fac(x):
    fact = 1
    for i in range(x,0,-1):
        fact = fact*i
    return fact
print(f'{fac(n)/(fac(k)*fac(r)):.0f}')
