def fibo3(n):
    f = [0,0,0,0,3,5]
    for i in range(6,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

A = int(input())
print(fibo3(A),A-2)