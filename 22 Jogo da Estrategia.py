#1940
Jogadores, Rodadas = map(int, input().split())
Entrada_Pontuacao = list(map(int, input().split())) 
Pontos = [0] * Jogadores 
for i in range(Jogadores):
    Pontos[i] = sum(Entrada_Pontuacao[i::Jogadores]) 
Pontos = Pontos[::-1]
Vencedor = Jogadores - Pontos.index(max(Pontos))
print(Vencedor)