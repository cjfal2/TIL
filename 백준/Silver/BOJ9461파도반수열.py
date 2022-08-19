F = [0,1,1,1,2,2,3,4,5,7,9] + [0]*200
for n in range(10,121):
    F[n] = F[n-2] + F[n-3]
for _ in range(int(input())):
    print(F[int(input())])