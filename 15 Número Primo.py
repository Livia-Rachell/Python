"""def conta_divisores_rec(n, d):
    if(d==1):
        return 1
    qtd = conta_divisores_rec(n, d-1)
    if (n%d==0):
        qtd = qtd+1
    return qtd

def num_primos(n):
    qtd_divisores = conta_divisores_rec(n,n)
    if (qtd_divisores == 2):
        r = "eh"
    else:
        r = "nao eh"
    return r"""
#Daqui para baixo
#1165
m = int(input())
for i in range(m):
    qtd = 0
    n = int(input())
    for i in range(1, n + 1):
        if(n%i == 0):
            qtd += 1
    if (qtd == 2):
        r = "eh"
    else:
        r = "nao eh"
    print("{} {} primo".format(n, r))