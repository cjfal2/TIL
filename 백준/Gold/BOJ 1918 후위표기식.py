Q = input()
B = ['+', '-', '*','/', '(', ')']
pi = []
buho = []


for i in Q:
    if i not in B :
        pi.append(i)
    elif i == '(':
        buho.append(i)
    elif i == '*' or i == '/':
        if buho != []:
            if buho[-1] == '*' or buho[-1] == '/':
                A = buho.pop()
                pi.append(A)
        buho.append(i)
        
    elif i == '+' or i == '-':
        if buho == []:
            buho.append(i)
        else:
            if '(' in buho:
                while buho[-1] != '(':
                    A = buho.pop()
                    pi.append(A)
                buho.append(i)
            else:
                while buho!=[]:
                    A = buho.pop()
                    pi.append(A)
                buho.append(i)
    elif i == ')':
        while buho[-1] != '(':
            A = buho.pop()
            pi.append(A)
        buho.pop()
while buho != []:
    if buho != []:
        A=buho.pop()
        pi.append(A)
    else:
        break
print(*pi,sep='')