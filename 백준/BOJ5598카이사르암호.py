word = list(map(ord,input()))
for i in range(len(word)) :
    if word[i] < 68 :
        word[i] = word[i] + 23
    else :    
        word[i] = word[i] - 3
print(*list(map(chr,word)),sep='') 