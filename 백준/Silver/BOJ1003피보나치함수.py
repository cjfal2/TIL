base0 = [0 for _ in range(41)]
base1 = [0 for _ in range(41)]
for tc in range(int(input())):
    base0[0] = 1
    base1[1] = 1

    N = int(input())
    if N > 1 :
        for i in range(2,N+1):
            base0[i] = base0[i-1] + base0[i-2]
            base1[i] = base1[i-1] + base1[i-2]
    print(base0[N],base1[N])