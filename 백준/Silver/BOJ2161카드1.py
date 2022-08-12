def cut(arr):
    return arr[0], arr[1:]

def mit(arr):
    t = arr[0]
    arr.append(t)
    arr.pop(0)
    return arr[1:]

N = int(input())
cards = [i for i in range(1,N+1)]
L = []
for x in range(N-1):
    T , cards = cut(cards)
    
    L.append(T)
    if len(cards) != 1 :
        mit(cards)

print(*L,cards[0],sep=" ")