from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    que=[]
    for i in range(n):
        for j in range(j):
            if graph[i][j] > 0 :
                que.append((graph[i][j],0,i,j))
            
    que.sort()
    queue=deque(que)

    while queue:
        virus,sec,y,x=queue.popleft()
        if sec == s :
            return 
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dy[i]
            if ny>=0 and nx>=0 and ny<y and nx<