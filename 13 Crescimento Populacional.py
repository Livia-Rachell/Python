#1160
n_Casos = int(input())
qtd = 0
aumento_ano_a = 0
aumento_ano_b = 0

for i in range(1, n_Casos + 1):
    pop_a, pop_b, cresc_a, cresc_b = map(float, input().split())
    qtd = 0

    while (pop_a <= pop_b):
        aumento_ano_a = (pop_a * cresc_a) // 100 
        aumento_ano_b = (pop_b * cresc_b) // 100 

        pop_a = pop_a + aumento_ano_a 
        pop_b = pop_b + aumento_ano_b 
        qtd = qtd + 1

    if (qtd <= 100):
        print("{:d} anos.".format(qtd))
    else:
        print("Mais de 1 seculo.")
