import sys
input = sys.stdin.readline

live = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for _ in range(int(input())):
    floor = int(input())
    ho = int(input())
    L = live[:ho]
    for f in range(floor):
        M = L[:]
        for idx,h in enumerate(range(ho)):
            L[idx] = sum(M[:idx+1])
    print(L[ho-1])