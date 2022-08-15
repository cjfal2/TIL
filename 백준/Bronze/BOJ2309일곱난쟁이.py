nan = []
for u in range(9):
    nan.append(int(input()))

jjin = []
for i in nan :
    nantest1 = nan[:]
    nantest1.remove(i)
    for j in nantest1 :
        nantest2 = nantest1[:]
        nantest2.remove(j)
        jjin.append((nantest2,sum(nantest2)))

for (x,y) in jjin:
    if y == 100 :
        for k in sorted(x):
            print(k)
        break
