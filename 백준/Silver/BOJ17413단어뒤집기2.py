# from collections import deque
# mystack = deque()
# text = deque(input())
# imsi = []

# while len(text) > 0  :

#     if text[0] == '<' :
#         e = text.index('>')
#         for _ in range(e+1):
#             mystack.append(text[0])
#             text.popleft()

#     else :
#         imsi.append(text.popleft())
        
#         if len(text) == 1 :
#             imsi.append(text.popleft())
#             imsi = imsi[::-1]
#             for i in imsi :
#                 mystack.append(i)

#         elif text[0] == ' ' or text[0] == '<'  :
            
#             imsi = imsi[::-1]
#             for i in imsi :
#                 mystack.append(i)
#             imsi = []
#             if text[0] == ' ' :
#                 mystack.append(' ')
#                 text.popleft()

# print(*mystack, sep='')
import sys
input = sys.stdin.readline

mystack = []
text = list(input().strip())
imsi = []

while len(text) > 0  :
		# '<' 를 만나면 그자리에서부터 > 까지 그냥 어펜드
    if text[0] == '<' :
        e = text.index('>')
        for _ in range(e+1):
            mystack.append(text[0])
            text.pop(0)
		# <> 사이가 아닐 경우
    else :
        imsi.append(text.pop(0))  #일단 임시저장소에 어펜드
        # 마지막 글자일 경우는 따로 처리
        if len(text) == 1 :
            imsi.append(text.pop(0))
            imsi = imsi[::-1]
            for i in imsi :
                mystack.append(i)
				# pop과 동시에 어펜드를 했으니까 다시 첫번째를 확인해서
				# 공백이나 < 일 경우 imsi를 뒤집어서 mystack에 어펜드
        elif text[0] == ' ' or text[0] == '<'  :
            
            imsi = imsi[::-1]
            for i in imsi :
                mystack.append(i)
            imsi = []              # 다시 imis는 초기화한다
            if text[0] == ' ' :   # 혹시 공백이었을 경우 공백을 줘야하므로 mystack에 공백을 어펜드하고 text에서는 pop (<는 위에 조건에서 써야하므로 살려야만 한다.)
                mystack.append(text.pop(0))

print(*mystack, sep='')