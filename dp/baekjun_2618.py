# 백준 2618
import sys
input = sys.stdin.readline

n = int(input())
w = int(input())
a_list = []
dp = [[-1] * (w + 1) for _ in range(w + 1)]
for _ in range(w):
    x, y = map(int, input().split())
    a_list.append((x, y))
    
p1 = [(1, 1)] + a_list
p2 = [(n, n)] + a_list

def find_a(p1,p2,n,w):
    if 


