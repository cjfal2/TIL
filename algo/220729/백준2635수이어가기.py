num = int(input())
ran = range(num//2,num+1)
relay_fin = []
relay = [num]
for i in ran :
    relay.append(i)
    while True :
        if relay[-2]-relay[-1] < 0 :
            break
        else :
            relay.append(relay[-2]-relay[-1])
    relay_fin.append((relay,len(relay)))
    relay = [num]
big = 0
big_index = 0
for idx in range(len(relay_fin)):
    big = max(big,relay_fin[idx][-1])
    if big == relay_fin[idx][-1] :
        big_index = idx
print(big)
print(*relay_fin[big_index][0])
