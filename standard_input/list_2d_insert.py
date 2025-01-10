# N = row 수
# 구조가 행이 N개인 배열의 리스트 입출력
import sys

input = sys.stdin.readline

N = int(input().strip())

list_2d = []

for i in range(N):
    col_list = list(map(int, input().split()))
    list_2d.append(col_list)
print(list_2d)