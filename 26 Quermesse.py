#2189
n = int(input())
l = list(map(int,input().split()))
v = 1
for i in range(len(l)):
    if l[i] != n:
        p = ('Teste', v)
        n = l[i]==n
        v = v + 1
    elif lista[i] == n:
        p = ('Teste', v)
        n = n
print(p, n)
    
