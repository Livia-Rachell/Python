#1789
while(True):
    try:
        n = int(input())
        v = list(map(int, input().split()))
        N = 0
        maior = max(v)
        if maior < 10:
            N = 1
        if maior >= 10 and maior <20:
            N = 2
        if maior >= 20:
            N = 3
        print(N)
    except EOFError:
        break