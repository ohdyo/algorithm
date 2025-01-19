from collections import deque
import sys

input = sys.stdin.readline

def priority_queue():
    queue = deque()
    n = int(input())  # 명령 개수 입력
    for _ in range(n):
        command = input().strip()
        if command.startswith("enqueue"):
            _, value = command.split()
            queue.append(int(value))
            queue = deque(sorted(queue, reverse=True))  # 우선순위 정렬
        elif command == "dequeue":
            if queue:
                print(queue.popleft())
            else:
                print("Empty")

# 실행
priority_queue()
