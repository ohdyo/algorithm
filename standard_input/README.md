 # Standard Input
## function -> input()

- Java의 Scanner 객체와 유사
- input의 경우 사용자의 입력을 읽어오고 전처리 과정이 존재
  1. 사용자의 입력을 받음
  2. 개행 문자 '\n'을 제거 !!
  3. 문자열 변경 후 return
  4. 입력이 없는 경우 에러 경고 


## library -> sys.stdin.readline()

- Java의 BufferReader와 유사
- readlin()의 경우 사용자의 입력을 읽어오고 전처리 과정이 없음
    1. 사용자의 입력을 받음
    2. Buffer에 저장 후 요청시 바로 읽어서 return
    3. 입력 없을 시 빈 문자열 반환

|          | input() | sys.stdin.readline() |
|----------|---------|----------------------|
| 개행('\n') | 제거 O    | 제거 X                 |
| 빈 입력     | 에러 출력   | 빈 문자열 출력             |

### 결국 전처리 과정과 오류 처리가 존재하는 input()이  효율이 더 떨어져 sys를 사용한다.

---

# 입력값을 받기 위해 알아야할 함수
## 1. split()
  - 입력 값 사이의 띄어쓰기를 구분해서 문자열을 나눈다.
```python
s = 'a b c d e f'
r = s.split() #인자값을 입력하면 해당 인자를 기준으로 나눔
print(f's.split() : {r}') #s.split() : ['a', 'b', 'c', 'd', 'e', 'f', ]
```
## 2. strip()
  - 시작과 끝 전부 개행 문자와 띄어쓰기를 제거해줄때 주로 사용한다.
```python
string = "         abcde         " 
string.strip()  # 'abcde' , ()안에 값이 있다면 해당 문자와 개행, 띄어쓰기 전부 제거하고 출력
```
## 3. map()
  - map(function, iterable) : 데이터 집합(=iterable)의 각 요소에 적용할 함수(function)을 인자로 가지고 각 요소에 함수 적용시켜서 결과 반환
  - 주로 알고리즘 문제에선 입력값들을 원하는 자료형으로 바꿀때 사용한다.
```python
s = ['1','2','3','4','5',]
data = list(map(int,s)) #
print(data) # [1,2,3,4,5]
# 몰라도 상관없는 이야기 : 사실 int는 클래스지만 int클래스 생성자를 호출하여 사용한 것
```

---

# 다양한 입출력 예제
# 초급
## 1. N개의 정수를 한 줄로 입력받기
```python
import sys

input = sys.stdin.readline
data = list(map(int, input().split()))
print(data)
```
## 2. 1차원 리스트에 입력값 저장 및 출력
```python
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 입력으로 주어진 숫자 N개의 합을 출력

```


---
# 중급
## 1. 특정 조건에 맞는 값 출력
- 한 줄에 정수 N과 정수 M을 입력한다.
- 다음 줄에 N개의 정수를 입력 받는다.
- 이 중 M보다 작은 수만 공백으로 구분해 출력한다.
```python
# 입력
5 3
4 2 1 5 3
#출력
2 1
```
## 2.. 2차원 리스트에 입력값 저장
```python
# N = row 수
# 구조가 행이 N개인 배열의 리스트 입출력
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
```
---
# 상급
# 1. 특정 조건에 따라 출력 형식 변경
- 정수 N과 정수 M을 입력받는다.
- 이 후 아래부터 N X M 형태의 이차원 배열을 입력한다.
- 홀수 행은 각 열을 더한 값을, 짝수 행은 각 열을 곱한 값을 계산한다.
- 각 인덱스의 값에 맞게 1차원 리스트로 계산된 값을 출력한다.
```python
# 입력
3 4
1 2 3 4
5 6 7 8
9 10 11 12
# 출력
[10,1680, 42]
import sys
input = sys.stdin.readline

# 정수 N과 M 입력받기
N, M = map(int, input().split())

# 2차원 리스트 입력받기
list_2d = [list(map(int, input().split())) for _ in range(N)]

# 결과를 저장할 리스트
result = []

# 홀수 행: 각 열의 합, 짝수 행: 각 열의 곱 계산
for i in range(N):
    if (i + 1) % 2 == 1:  # 홀수 행 (인덱스 기준 1부터 시작)
        row_sum = sum(list_2d[i])
        result.append(row_sum)
    else:  # 짝수 행
        row_product = 1
        for num in list_2d[i]:
            row_product *= num
        result.append(row_product)

# 결과 출력
print(result)

```
# 2. 데이터 필터링
- 정수 N과 M을 입력받는다.
- N X M 크기의 2차원 리스트를 입력받는다.
- 각 행에서 짝수만 남기고 출력한다.
```python
# 입력
3 4
1 2 3 4
5 6 7 8
9 10 11 12
# 출력
2 4
6 8
10 12
# 정수 N과 M 입력받기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 2차원 리스트 입력받기
matrix = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
for row in matrix:
    # 짝수만 남기기
    even_numbers = [num for num in row if num % 2 == 0]
    # 결과 출력
    print(*even_numbers)

```
# 3 행렬 회전
- N을 입력받는다.
- N X N크기의 행렬을 입력받는다.
- 90도 회전해서 값들을 이동시킨다.
```python
# 입력
3
1 2 3
4 5 6
7 8 9
#출력
7 4 1
8 5 2
9 6 3
```
---
### 혼틈 노드와 간선 간략 설명!

- 노드는 내가 가야할 장소
- 간선은 지금 내가 있는 노드에서 다른 노드로 갈수 있게 해주는 다리
---
# 한번 풀면 나중에 다른 알고리즘에서 적용될 정렬
## 4. 노드별 연결된 해당 노드, 입출력
<img width="275" src="https://velog.velcdn.com/images/khyun11/post/aa8cef39-7fa1-4ef2-b5d7-55ffad6eba43/image.png">

입력
```python
# 입력부
5 7
0 1
0 4
1 2
1 3
1 4
2 3
3 4
# 출력부
[
  [1, 4], # 0번쨰 노드와 연결된 다른 노드
  [0, 2, 3, 4], # 1번쨰 노드와 연결된 다른 노드
  [1,3,4], # 2번쨰 노드와 연결된 다른 노드
  [1,2,4], # 3번쨰 노드와 연결된 다른 노드
  [0,1,3] # 4번쨰 노드와 연결된 다른 노드
]
#
import sys

input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n)] 

# 그래프 구성
# 입력받은 값들을 인덱스의 번호를 노드로 삼아 해당 노드와 연결된 다른 노드들로 표현되도록 변경
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)

```

## 5. 노드별 연결된 해당 노드,가중치 입출력 
<img src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/201007/tttttt.png">

```python
# 입력부
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
# 출력부
[
  [],
  [(2, 3), (3, 2)],
  [(1, 3), (4, 5)], 
  [(1, 2), (5, 11), (6, 9)], 
  [(2, 5), (7, 1), (8, 7)], 
  [(3, 11), (9, 15), (10, 4)],
  [(3, 9), (11, 6), (12, 10)], 
  [(4, 1)], [(4, 7)], [(5, 15)],
  [(5, 4)], [(6, 6)], [(6, 10)]
]
#
import sys

#입력부
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
print(graph)
```
