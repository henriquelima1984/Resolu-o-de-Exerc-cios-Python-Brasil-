# 4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
# que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

populacao_a = 80_000
populacao_b = 200_000
taxa_de_crescimento_de_a = 1.03
taxa_de_crescimento_de_b = 1.015
anos = 0

while True:
    while populacao_a < populacao_b:
        print(f'{anos} ano(s)')
        print(f'População A -> {populacao_a} habitantes')
        print(f'População B -> {populacao_b} habitantes')
        anos += 1

        populacao_a = int(populacao_a * taxa_de_crescimento_de_a)
        populacao_b = int(populacao_b * taxa_de_crescimento_de_b)

        print(f'{anos} ano(s)')
        print(f'População A -> {populacao_a} habitantes')
        print(f'População B -> {populacao_b} habitantes')
