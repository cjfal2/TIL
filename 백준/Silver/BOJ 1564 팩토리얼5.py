def fac(N):
    if N == 0 or N == 1:
        return 1
    else:
        z = 1
        for i in range(1,N+1):
            z*=i
            while str(z)[-1] == '0':
                z//=10
            if len(str(z)) > 20:
                z = int(str(z)[-20:])
            
        return str(z)[-5:]

N = int(input())

print(fac(N))