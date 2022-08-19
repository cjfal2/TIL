for _ in range(int(input())):
    L = {}
    for _ in range(int(input())):
        A , B = input().split()
        if B not in L :
            L[B] = [A]
        else :
            L[B].append(A)
    co = 1
    for i in L.values():
        co *= len(i)+1
    print(co-1)