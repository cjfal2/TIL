N , M = map(int,input().split())
card = list(map(int,input().split()))
L = []
for i in range(N):
    for j in range(i+1,N):
        if j == N-1 :
            continue
        else :
            if j == N-2 and card[i]+card[j]+card[-1] <= M:
                L.append(card[i]+card[j]+card[-1])
            else:
                for k in range(j+1,N):
                    if card[i]+card[j]+card[k] <= M :
                        L.append(card[i]+card[j]+card[k])
print(max(L))