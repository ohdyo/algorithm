import sys

readline = sys.stdin.readline

sentence = list(map(str, readline().split()))
print(len(sentence))