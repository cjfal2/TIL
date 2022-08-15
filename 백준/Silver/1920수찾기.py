import sys
input = sys.stdin.readline

def binary(a,key):
	low_idx = 0
	high_idx = len(a)-1
	while low_idx <= high_idx:
		mid_idx = int((low_idx + high_idx)/2)
		if key == a[mid_idx]:  #검색 성공
			return 1
		elif key < a[mid_idx] :
			high_idx = mid_idx - 1
		elif key > a[mid_idx]:
			low_idx = mid_idx + 1
	return 0


N = int(input())
A = sorted(list(map(int,input().split())))

M = int(input())
B = list(map(int,input().split()))

for key1 in B :
    print(binary(A,key1))