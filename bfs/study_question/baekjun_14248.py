from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))
start = int(input()) -1

cnt = 1
visited = set()

def dfs(idx):
    global cnt
    visited.add(idx)

    for next_idx in (idx - stones[idx], idx + stones[idx]):
        if 0<= next_idx and next_idx < n and next_idx not in visited:
            cnt += 1
            dfs(next_idx)

dfs(start)
print(cnt)