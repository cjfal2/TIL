# def soinsu(n):
#     sosu = 2 
#     sosu_list = []
#     while (sosu**2 <= n): 
#         while (n % sosu == 0):
#             sosu_list.append(sosu) 
#             n = n // sosu 
#         sosu += 1
#     if n > 1 : 
#         sosu_list.append(n)
#     return sosu_list
T = int(input())

for tc in range(1,T+1):
    num = int(input())

    L = [2,3,5,7,11]
    counts = []
    for sosu in L:
        c = 0
        while True :
            if num%sosu == 0 :
                c += 1
                num = num//sosu
            else :
                counts.append(c)
                break
    J = ' '.join(map(str,counts))
    print(f'#{tc} {J}')