# 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
result = [0] * 10001 # 이렇게 초기화하면 성공
# result = [0] * n  # 이렇게 초기화하면 메모리 초과 

for _ in range(n) :
    result[int(sys.stdin.readline())] += 1

for idx in range(10001) :
    for n in range(result[idx]):
        print(idx)