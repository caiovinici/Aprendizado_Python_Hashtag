# Instrutura do If

faturamento = 1000
custo = 8100
lucro = faturamento - custo

if lucro >= 0:
    # tudo qe a condicao for verdadeira
    print('Lucro:', lucro)
else:
    # tudo que a condicao for falsa
    print('Prejuizo!', lucro)


produtos = ['iphone', 'ipad', 'airpod']
novo_produto = input('Digite aqui o produto:').lower().strip()

if novo_produto in produtos:
    print('Produto já cadastrado')
else:
    print('Produto cadastrado com sucesso!')
    produtos.append(novo_produto) # append implementa algo na lista
print(produtos)


# acimda de 15000 -> 500 de bonus
# acimda de 10000 -> 150 de bonus
# acimda de 5000 -> 50 de bonus
vendas = 10000
if vendas > 15000:
    bonus = 500
# caso contrario, se for maior que 10.000
elif vendas > 10000:
    bonus = 150
elif vendas > 5000:
    bonus = 50
else:
    bonus = 0
print('Bonus', bonus)


vendas_01 = 17000
vendas_empresa = 6000
metas_empresa = 5000

# .not - string de negar condicao
#.or(ou)
if vendas_01 > 15000 and vendas_empresa > metas_empresa: #.and( e )
    bonus = 500
elif vendas_01 > 10000:
    bonus = 150
elif vendas_01 > 5000:
    bonus = 50
else:
    bonus = 0
print('Bonus', bonus)

