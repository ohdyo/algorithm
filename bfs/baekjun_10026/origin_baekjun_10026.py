import sys
from collections import deque
import copy

drow = [-1,1,0,0]
dcol = [0,0,-1,1]

def bfs(row,col,visited,graph):
    que = deque()
    que.append((row,col))
    visited.add((row,col))
    
    while que:
        row, col = que.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if 0<= nrow and nrow <n and  0<= ncol and ncol <n :
                if (nrow,ncol) not in visited: 
                    if graph[nrow][ncol] == graph[row][col] :
                        que.append((nrow,ncol))
                        visited.add((nrow,ncol))
                        
def checking_area(n,graph):
    result = [0,0]
    tmp_graph = copy.deepcopy(graph)
    
    visited = set()
    for i in range(n): 
        for j in range(n):
            if (i,j) not in visited:
                bfs(i,j,visited,graph)
                result[0] += 1
    
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] == 'G':
                tmp_graph[i][j] = 'R'
    other_visited = set()
    for i in range(n):
        for j in range(n):
            
            if (i,j) not in other_visited:
                bfs(i,j,other_visited,tmp_graph)
                result[1] += 1
    return result


input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(str, sys.stdin.readline().strip()))) 

print(checking_area(n,graph))
