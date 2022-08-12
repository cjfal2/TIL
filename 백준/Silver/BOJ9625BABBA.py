N = int(input())

H = 'A'
for i in range(N):
    h = H.replace('A','b')
    k = h.replace('B','BA')
    m = k.replace('b','B')
    H = m

print(H.count('A'),H.count('B'))