A = int(input())
if A%2 :
    tape = 0
    for i in range(0,A,2):
        tape += 2**i
else :
    tape = 1
    for i in range(1,A,2):
        tape += 2**i
print(tape%10007)