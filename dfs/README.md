Depth-First-Search - 깊이 우선 탐색
노드(node = Vertex)와 간선(Edge)으로 그래프를 표현
위에서 아래로 찾는 방식
가장 마지막에 만났던 정점으로 돌아가 다시 탐색하는 LIFO구조의 스택 사용
**스택과 재귀 알고리즘의 형태로 구현 가능**

**재귀 함수의 기본 형식**
### dfs 정의된 코드
```
# DFS 함수 정의 (visited = [])
def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            
# DFS 함수 정의2 (visited = set())
def dfs(node):
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node)
```
* 적용중인 그래프의 노드를 순회하기 위해 visited함수에서 방문한 노드를 검증하면서 순회한다.
- **최단 경로라는 보장이 없음**
- 경로의 함정에 빠지는 경우가 있음

### 노드별 연결된 다른 노드
```
# 노드 번호가 1부터 시작하므로 크기 n+1
graph = [[] for _ in range(n + 1)]  

# 그래프 구성
# 입력받은 값들을 인덱스의 번호를 노드로 삼아 
# 해당 노드와 연결된 다른 노드들로 표현되도록 변경
# 간선의 갯수(m)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
```
* 입력받은 노드별 연결구간을 해당하는 인덱스의 노드마다 연결된 다른 노드를 볼수 있도록 해주는 방식
## 사용 구역
* 미로 탐색 문제
* 경로의 특징을 저장해야하는 경우
* 검색 대상 그래프가 많을 때 최단 거리 찾기(노드가 적으면 BFS가 효율적)
```
def dfs_recursive(graph, start, visited = []):
	## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
    visited.append(start)
 	
    # start노드부터 순회하여 깊이탐색 후 방문기록을 남기기 위해 재귀호출함
    # 전체 순환이 완료했으면 return으로 visited에 담긴 순서의 리스트 반환
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited
```
## 문제1 (백준 14888)
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.

1+2+3-4×5÷6
1÷2+3+4-5×6
1+2÷3×4-5+6
1÷2×3-4+5+6
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

1+2+3-4×5÷6 = 1
1÷2+3+4-5×6 = 12
1+2÷3×4-5+6 = 5
1÷2×3-4+5+6 = 7
N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.

출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

### 풀이 방식
* 해당 문제의 경우 **숫자는 고정**한 상태에서 수식만 움직이면서 모든 경우에 해당하는 최댓값과 최솟값을 구하는 문제이다.
* 그를 위한 전체 탐색 알고리즘을 생각하고 bfs 혹은 dfs로 구상이 가능하다.
```
import sys

input = sys.stdin.readline

#입력부부
N = int(input())
num = list(map(int,input().split()))
plus,minus,multi,divide = map(int,input().split())


# 탐색을 위한 dfs 정의
# n = 경유 노드
# sm = 재귀 동안의 계산 결과 값
# add-sub-mul-div 구간 마다의 계산 수식
# mn, mx = 최대 최소 값값 
def dfs(n,sm,add,sub,mul,div):
    global mn, mx
    
    if sm < int(-1e9) or int(1e9) < sm:
        return
    
    # 마지막 분기
    # 도착시 함수 종료(무한루프방지)
    if n==N:
        mn = min(mn,sm)
        mx = max(mx,sm)
        return
    
    # 분기 시작
    # i) 처음 호출시(재귀호출X) add값이 존재한다면 조건 실행후 재귀 호출
    # ii) 처음 호출한 함수가 add조건을 지나 sub로 내려가서 해당 조건 충족시 재귀 호출
    # iii) 위의 방식과 마찬가지로 곱하기 나누기 진행
    # iV) 이렇게 처음 호출한 함수가 모든 조건을 충족한다면 최대4갈래의 분기로 나뉘면서 재귀 호출을 진행함함
    if add>0:
        dfs(n+1,sm+num[n],add-1,sub,mul,div)
    if sub>0:
        dfs(n+1,sm-num[n],add,sub-1,mul,div)
    if mul>0:
        dfs(n+1,sm*num[n],add,sub,mul-1,div)
    if div>0:
        dfs(n+1,int(sm/num[n]),add,sub,mul,div-1)
    
mn, mx = int(1e9),int(-1e9) 

dfs(1,num[0],plus,minus,multi,divide)

print(mx,mn,sep='\n')

```

## 문제2 (백준 18428)
https://www.acmicpc.net/problem/18428
NxN 크기의 복도가 있다. 복도는 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 선생님, 학생, 혹은 장애물이 위치할 수 있다. 현재 몇 명의 학생들은 수업시간에 몰래 복도로 빠져나왔는데, 복도로 빠져나온 학생들은 선생님의 감시에 들키지 않는 것이 목표이다.

각 선생님들은 자신의 위치에서 상, 하, 좌, 우 4가지 방향으로 감시를 진행한다. 단, 복도에 장애물이 위치한 경우, 선생님은 장애물 뒤편에 숨어 있는 학생들은 볼 수 없다. 또한 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다고 가정하자.

다음과 같이 3x3 크기의 복도의 정보가 주어진 상황을 확인해보자. 본 문제에서 위치 값을 나타낼 때는 (행,열)의 형태로 표현한다. 선생님이 존재하는 칸은 T, 학생이 존재하는 칸은 S, 장애물이 존재하는 칸은 O로 표시하였다. 아래 그림과 같이 (3,1)의 위치에는 선생님이 존재하며 (1,1), (2,1), (3,3)의 위치에는 학생이 존재한다. 그리고 (1,2), (2,2), (3,2)의 위치에는 장애물이 존재한다. 

![](https://velog.velcdn.com/images/ohdyo/post/5acfbeb1-b5d8-4513-8026-a2fa0daad327/image.png)


이 때 (3,3)의 위치에 존재하는 학생은 장애물 뒤편에 숨어 있기 때문에 감시를 피할 수 있다. 하지만 (1,1)과 (2,1)의 위치에 존재하는 학생은 선생님에게 들키게 된다.

학생들은 복도의 빈 칸 중에서 장애물을 설치할 위치를 골라, 정확히 3개의 장애물을 설치해야 한다. 결과적으로 3개의 장애물을 설치하여 모든 학생들을 감시로부터 피하도록 할 수 있는지 계산하고자 한다. NxN 크기의 복도에서 학생 및 선생님의 위치 정보가 주어졌을 때, 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력하는 프로그램을 작성하시오.

* 예시 입력
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

```
# 생각
# 학생들이 선생님의 상,하,좌,우에 안보이게끔 시야만 잡아준다
# 선생님의 입장에서 상 하 좌 우 끝까지 깊이 있게 탐색을 위해 dfs
# 해당 경우는 최단의 경우보다 가능한 경우를 찾는거이에 dfs 활용

# 코드 순서
# 1. 벽 세우기 위한 함수 및 재귀함수로 구현(build_wall)
# 2. 벽을 3번 세웠으면 결과 값 반환 함수 구현(find_result)
# 3. 결과 값 반환에 필요한 조건에 대한 함수 구현(search_s)

import sys

#입력부
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(str, input().split())))

# 결과값 반환
def find_result(graph) :
    #선생님 찾기
    for row in range(n):
        for col in range(n):
            if graph[row][col] == 'T':
                #위치 파악한 노드의 인덱스번호를 이용해서 학생 찾기 시작
                result = search_s(row,col)
                if result == False:
                    return False
    return True

# 학생 찾기
def search_s(row,col) :
    #상 하 좌 우 나눠서 파악
    for i in range(1,n):
        if row-i>=0:
            if graph[row-i][col] == 'O':
                break
            elif graph[row-i][col] == 'S':
                return False

    for i in range(1, n):
        if row+i<n:
            if graph[row+i][col] == 'O':
                break
            elif graph[row+i][col] == 'S':
                return False

    for i in range(1, n):
        if col-i>=0:
            if graph[row][col-i] == 'O':
                break
            if graph[row][col-i] == 'S':
                return False

    for i in range(1, n):
        if col+i<n:
            if graph[row][col+i] == 'O':
                break
            if graph[row][col+i] == 'S':
                return False
    return True

#벽을 세울수 있는 경우의 수 탐색
def build_wall(wall,graph):
    if wall == 3:
        result = find_result(graph)
        if result == True:
            print('YES')
            ## 코드 종료 함수
            exit()
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                build_wall(wall+1,graph)

build_wall(0,graph)
print('NO')
```

## 문제 3(백준 11724)
https://www.acmicpc.net/problem/11724
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
### 풀이 방식
* 결국 각 노드별 연결된 노드를 확인하는게 우선
* 연결된 노드를 순회하는 과정에서 방문 기록을 남겨야 함
* 연결된 노드를 순회하고 마치면 재귀함수가 종료되고 하나의 영역을 순회 완료
* 다른 영역을 탐색할수 있도록 방문 기록에 포함되지 않는 노드도 탐색할수 있도록 구현
```
import sys

input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 노드 번호가 1부터 시작하므로 크기 n+1

# 그래프 구성
# 입력받은 값들을 인덱스의 번호를 노드로 삼아 해당 노드와 연결된 다른 노드들로 표현되도록 변경
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)

visited = set()  # 방문 기록 리스트

# DFS 함수 정의
def dfs(node):
    visited.add(node)
    for next_node in graph[node]:
        if next_node not in visited:
            dfs(next_node)

# 연결 요소 개수 계산
count = 0
for i in range(1, n + 1):  # 노드 번호가 1부터 시작
    if i not in visited:  # 방문하지 않은 노드에서 DFS 시작
        dfs(i)
        print(visited)
        count += 1

print(count)
```
## 문제4 (백준 24480)
https://www.acmicpc.net/problem/24480
오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 내림차순으로 방문한다.

첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.

다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.
### 풀이 방법
* 입력 받은 노드와 간선을 노드별로 정리하도록 코드 구현
* 방문기록은 set으로 방문 분서는 리스트로 구현해서 순서를 기록

```
import sys

#입력부
input = sys.stdin.readline
N, M, R = map(int,input().split())
graph=[[] for _ in range(N + 1)]


#인덱스별 인접 노드 정리
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 각 노드별로 연결된 노드들을 정렬
for i in range(1, N + 1):
    graph[i].sort(reverse=True) 
print(graph)

#방문기록 & 최종 결과는 dfs 탐색 순서이므로 set과 리스트 선언언
visited = set()
result = []

def dfs(graph,S):
    if S in visited:
        return 0
    visited.add(S)
    result.append(S)
    for next_node in graph[S]:
        if next_node not in visited:
            dfs(graph, next_node)


for i in range(1, N+1):
    if i not in visited:
        dfs(graph,R)

print(result)
```
