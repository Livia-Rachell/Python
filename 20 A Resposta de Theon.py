#1858
n = int(input())
l = list(map(int, input().split()))
print(l.index(min(l)) + 1)