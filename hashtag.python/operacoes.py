faturamento = 1000
custo = 700

novas_vendas = 300

faturamento = faturamento + novas_vendas # somar
imposto = faturamento * 0.1 # multiplicar
lucro = faturamento - custo - imposto # subtrair

print(f'Faturamento: R$ {faturamento:.2f}')
print(f'Lucro: R$ {lucro:.2f}')

margem_lucro = lucro / faturamento # dividir

print(f'Margem de lucro: R${margem_lucro:.2f}')

restituicao = imposto * 0.1
print(f'Restituição: R$ {restituicao:.2f}')

# Mod resto da divisao %
# 10 % 3
tempo_em_meses = 160
tempo_em_anos = int(tempo_em_meses / 12)
print(f'\nAnos: {tempo_em_anos} Meses: {tempo_em_meses % 12}')

numero = 123.57

# round - arredondamento do numero intera 123.57 -> 124
print(round(numero))

# usar _ parar fazer divisao visual nos numeros nao altera a string -> str
faturamento = 139_018_182
