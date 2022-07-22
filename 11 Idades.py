i = 0
lista = []
contador = 0
while (i >= 0):
    i = int(input())
    if (i >= 0):
        lista.append(i)
        contador += 1
print("{:.2f}".format(sum(lista)/contador))