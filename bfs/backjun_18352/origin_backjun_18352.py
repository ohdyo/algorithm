import sys
from collections import deque

# 1. 바이러스가 퍼지면서 모든 공간을 탐색한다.(BFS)
# 2. 초(=반복문)을 반복할때마다 상하 좌우로 바이러스가 움직인다.
# 3. 바이러스에는 수가 낮은은 개체가 우선순위를 가진다.

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]


# 정사각형 공간
def bfs(n,graph,s,y,x):
    que= []
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] >0:
                que.append((graph[i][j],0,i,j))
    
    que.sort()
    queue = deque(que)
    
    while queue:
        virus,sec,row,col = queue.popleft()
        if sec == s:
            return graph[y-1][x-1]
        for i in range(4):
            next_row = row + drow[i]
            next_col = col + dcol[i]
            if 0<=next_row<n and 0<=next_col<n :
                if graph[next_row][next_col] == 0:
                    graph[next_row][next_col] = virus
                    queue.append((graph[next_row][next_col],sec + 1, next_row, next_col))
    


# 입력부
n, k = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

s, y, x = map(int, sys.stdin.readline().split())

print(bfs(n,graph,s,y,x))


    
            
    
