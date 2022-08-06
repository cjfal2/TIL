for i in range(int(input())):
    A = list(input().split())
    for idx , word in enumerate(A) :
        A[idx] = word[::-1]
    print(*A)