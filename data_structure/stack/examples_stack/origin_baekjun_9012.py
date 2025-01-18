import sys

t = int(sys.stdin.readline())

for i in range(t):
    data = sys.stdin.readline()
    stack = list(data)
    result = 0

    for j in stack :
        if j == "(":
            result += 1
        elif j == ')':
            result -= 1
        
        if result < 0 :
            print("NO")
            break

    if result == 0: print('YES')
    else: print('NO')