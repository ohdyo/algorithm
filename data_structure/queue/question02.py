from collections import deque
import sys

input = sys.stdin.readline

def rotate_queue():
    n, k = map(int, input().split())  # N, K 입력
    queue = deque(range(1, n + 1))
    for _ in range(k):
        queue.append(queue.popleft())
    print(" ".join(map(str, queue)))

# 실행
rotate_queue()
