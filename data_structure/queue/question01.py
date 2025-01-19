from collections import deque
import sys

input = sys.stdin.readline

def basic_queue():
    queue = deque()
    n = int(input())  # 연산 개수 입력
    for _ in range(n):
        command = input().strip()
        if command.startswith("enqueue"):
            _, value = command.split()
            queue.append(int(value))
        elif command == "dequeue":
            if queue:
                print(queue.popleft())
            else:
                print("Empty")
        elif command == "front":
            if queue:
                print(queue[0])
            else:
                print("Empty")

# 실행
basic_queue()
