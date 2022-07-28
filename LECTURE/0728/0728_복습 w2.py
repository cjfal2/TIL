class wordrelay:
    def relay(self,WL):
        count = 1
        for i in range(1,len(WL)):
            count += 1
            if WL[i] in WL[:i]:
                return (f'{count}번째 참가자가 탈락하였습니다.')
            elif WL[i-1][-1] != WL[i][0]:
                return (f'{count}번째 참가자가 탈락하였습니다.')
        return('모두통과입니다.')




words = ["round","dream","magnet","tweet","twet","trick","kiwi"]
a = wordrelay()
print(a.relay(words)) # 5번째 참가자가 탈락하였습니다.
