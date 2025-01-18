# 재귀 함수 (recursion) & DP (동적 프로그래밍)

## 재귀 함수 (recursion)
- 자기 자신을 호출한다.
- 하나의 함수가 실행되는 동안 다른 함수가 안에서 동작한다.
- 반복을 통해서 나오는 값을 찾을 때 사용한다.


### 특징
- 재귀함수는 종료시점이 명확해야한다.
    - 명확하지 않으면 스택 오버플로 발생
```python
# 팩토리얼
def factorial(n):
    if n ==0 :
        reuturn 1
    return factorial(n-1) * n
```

---
### 예제
#### 리스트 뒤집기
```python
# 리스트 뒤집기

```

####  하노이 탑
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbv2YGx%2FbtroEzZxi2v%2F20GbP2aZqZNAebbMEganNk%2Fimg.png"/>

```python
# 하노이 탑

```