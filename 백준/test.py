a=int(input())
n=1
for i in range(1,a+1):
    n*=i
    if len(str(n))>20:
        n=int(str(n)[-20:])
    while str(n)[-1]=="0":
        n=int(str(n)[:-1])

n=int(str(n)[-5:])

print('%05d' %n)