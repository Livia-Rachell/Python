#1146
n = -1
while(n != 0):
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(1, n + 1):
        l.append(i)
    print(*l)