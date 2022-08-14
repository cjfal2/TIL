n = int(input())
num_list = []
for i in range(666, n*1000):
    test = str(i)
    if "666" in test:
        num_list.append(i)
    if len(num_list) == n:
        break
print(num_list[n-1])