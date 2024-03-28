# Estrutura de repetição

#for i in range(10):  # repete o print quantas vezes tiver na ()
    #print('Repetição')


lista_precos = [1500, 1000, 800, 2000]
# rodando todos os itens da lista
print('Somando Imposto 10%')
for preco in lista_precos:
    imposto = preco * 0.1
    print(f'Preço R${preco:.2f} --- Imposto R${imposto:.2f}')

print('===' * 15)


# preço até 1000 > imposto é de 10%
# preço maior de 1000 > imposto é de 15%
print('Maior valor & menor valor')
for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
        print(f'Preço R${preco:.2f} ---- Imposto R${imposto:.2f}')

print('====' * 15)


print('Somando total de imposto')
total_imposto = 0 # acumulado

for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    total_imposto = total_imposto + imposto
print(f'Total de Imposto R${total_imposto:.2f}')
