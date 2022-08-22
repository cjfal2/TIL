N = int(input())
Q = input()
ALPA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dic = {}
for i in ALPA[:N]:
    dic[i] = int(input())

B = ['+','-','*','/']
stack = []


for i in Q:
    if i not in B:
        stack.append(int(dic[i]))
    elif i == '+':
        z = 0
        z += stack.pop()
        z += stack.pop()
        stack.append(z)
    elif i == '-':
        z = 0
        z -= stack.pop()
        z += stack.pop()
        stack.append(z)
    elif i == '*':
        z = 1
        z *= stack.pop()
        z *= stack.pop()
        stack.append(z)
    elif i == '/':
        z = 1
        z /= stack.pop()
        z *= stack.pop()
        stack.append(z)
print(f'{stack[0]:.2f}')