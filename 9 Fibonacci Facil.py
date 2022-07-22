#1151
Num = int(input())
Fib = [0, 1]
for i in range(1, Num-1):
        P = Fib[i] + Fib[i - 1]
        if (P != Num):
            Fib.append(P)
        else:
            break
print(*Fib)