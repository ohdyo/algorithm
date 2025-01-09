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
  - map(function, iterable) : 데이터 집합(=iterable)의 각 요소에 적용할 함수(function)을 인자로 가지는 함수
  - 주로 알고리즘 문제에선 입력값들을 원하는 자료형으로 바꿀때 사용한다.
```python
s = ['1','2','3','4','5',]
data = list(map(int,s)) #
print(data) # [1,2,3,4,5]
# 몰라도 상관없는 이야기 : 사실 int는 클래스지만 int클래스 생성자를 호출하여 사용한 것
```

---

# 다양한 입출력 예제
## 1. N개의 정수를 한 줄로 입력받기
```python
import sys

read = sys.stdin.readline
data = list(map(int, read().split()))
print(data)
```
## 2. 1차원 리스트에 입력값 저장
```python

```
## 3. 2차원 리스트에 입력값 저장
```python

```

---
### 혼틈 노드와 간선 간략 설명!

- 노드는 내가 가야할 장소
- 간선은 지금 내가 있는 노드에서 다른 노드로 갈수 있게 해주는 다리
---
## 4. 노드별 연결된 해당 노드, 입출력
<img width="275" src="https://velog.velcdn.com/images/khyun11/post/aa8cef39-7fa1-4ef2-b5d7-55ffad6eba43/image.png">

```python

```

## 5. 노드별 연결된 해당 노드,가중치 입출력 
<img src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/201007/tttttt.png">

```python

```