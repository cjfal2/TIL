N = int(input())
M = int(input())
S = input()

count = 0
Pattern = 0
i = 1
while i < M-1:
  if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
    Pattern += 1
    if Pattern == N:
      Pattern -= 1
      count += 1   
    i += 1
  else:
    Pattern = 0
  i += 1
  
print(count)