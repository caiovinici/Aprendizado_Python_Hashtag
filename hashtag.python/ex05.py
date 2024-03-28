# Calculando Bônus de Vendas

vendas = {
    'André': [1000, 500, 300, 5000, 1500, 80, 3000],
    'Andressa': [1500, 9000, 300, 150, 120, 130, 55, 500, 8500],
    'Alan': [800, 100],
    'Ana': [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 200, 180],
}
# cada venda o vendedor ganha R$2 e 1% do valor da venda
# calcular o valor total de bonus pago e o bonus de cada vendedor
def calcular_bonus(lista_vendas):
    qntde = len(lista_vendas)
    bonus1 = qntde * 2
    valor_total = sum(lista_vendas)
    bonus2 = 0.01 * valor_total
    bonus = bonus1 + bonus2
    return bonus

bonus_total = 0
for vendedor in vendas:
    lista_vendas_vendedor = vendas[vendedor]
    bonus = calcular_bonus(lista_vendas_vendedor)
    print(f'Vendedor {vendedor} ---- Bônus R$ {bonus:.2f}')
    bonus_total = bonus_total + bonus
print(f'Bônus total R$ {bonus_total:.2f}')
print('=='*20)


for vendendor, lista_vendas in vendas.items(): # Fazendo Tuplas
    print(vendendor)
    print(lista_vendas)
