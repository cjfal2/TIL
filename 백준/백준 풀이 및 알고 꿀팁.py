import sys
input = sys.stdin.readline
sys.stdin = open('sample.txt','r')

N=int(input())

L = list(map(int,input().split()))
x , y = list(map(str,input().split()))
A = []
A.sort(key=lambda x:x[1]) #열 기준 정렬
A.sort(key=lambda x:x[0]) #행 기준 정렬
