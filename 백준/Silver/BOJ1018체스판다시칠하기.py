N , M = map(int,input().strip().split())
pan = [list(input()) for _ in range(N)]

whatmin = []
for n1 in range(N-7):
    for m1 in range(M-7):
        W_test = 0
        for n2 in range(0,8,2):
            for m2 in range(0,8,2):
                if pan[n1+n2][m1+m2] != 'W':
                    W_test += 1
                if pan[n1+n2][m1+m2+1] != 'B':
                    W_test += 1
                if pan[n1+n2+1][m1+m2] != 'B':
                    W_test += 1
                if pan[n1+n2+1][m1+m2+1] != 'W':
                    W_test += 1

        whatmin.append((W_test))

for n1 in range(N-7):
    for m1 in range(M-7):
        B_test = 0
        for n2 in range(0,8,2):
            for m2 in range(0,8,2):
                if pan[n1+n2][m1+m2] != 'B':
                    B_test += 1
                if pan[n1+n2][m1+m2+1] != 'W':
                    B_test += 1
                if pan[n1+n2+1][m1+m2] != 'W':
                    B_test += 1
                if pan[n1+n2+1][m1+m2+1] != 'B':
                    B_test += 1
                    
        whatmin.append((B_test))

print(min(whatmin))