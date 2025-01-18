import sys

input = sys.stdin.readline

string = str(input().strip())

def reverse_string(string):
    string = list(string)
    reversed_str = ""
    while string:
        reversed_str += string.pop()
    return reversed_str

print(reverse_string(string))