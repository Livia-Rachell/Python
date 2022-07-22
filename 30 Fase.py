#2663
NC = int(input())
Min_C = int(input())
Pontos = []
Clds = 0
Sub_pontos = []
for i in range(0, NC):
    Pontuacao = int(input())
    Pontos.append(Pontuacao)
Sub_pontos = sorted(set(Pontos))
Tamanho_Nova_Lista = len(Sub_pontos)
for i in range(0, Tamanho_Nova_Lista):
    while (Clds < Min_C):
        if (Pontos.count(max(Sub_pontos)) >= 2):
            Clds += Pontos.count(max(Sub_pontos))
            Sub_pontos.remove(max(Sub_pontos))
        elif (Pontos.count(max(Sub_pontos)) == 1):
            if (Clds < Min_C):
                Clds += 1
                Sub_pontos.remove(max(Sub_pontos))      
            else:
                break 
print(Clds)