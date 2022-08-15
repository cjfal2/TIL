import sys
N,M = map(int,sys.stdin.readline().split())
for i in range(min(N,M), 0, -1):
    if (N%i==0) and (M%i==0) :
        print(i)
        break
for i in range(max(N,M), (N*M) + 1):
	if i % N == 0 and i % M == 0:
		print(i)
		break


import math
import sys
N,M = map(int,sys.stdin.readline().split())
print(math.gcd(N,M))
print(math.lcm(N,M))
