vendas_22 = {'jan': 15000, 'fev': 15500, 'mar': 14000, 'abr': 16600, 'mai': 16300,
             'jun': 17000}
vendas_23 = {'jan': 17000, 'fev': 15000, 'mar': 17500, 'abr': 16900, 'mai': 16000,
             'jun': 18500}

# saber quanto variou percentualmente cade mes de 23 em 22
print('Variação Percentualmente')
print('--' * 15)

for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    var_percentual = valor_23 / valor_22 - 1
    print(f'Variação de {mes}: {var_percentual:.1%}') # formatação percentual
print('==' * 15)


# simular faturamento
print('\nSimulação Faturamento')
print('--' * 15)

faturamento = 0
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    var_percentual = valor_23 / valor_22 - 1
    if var_percentual < 0:# 2 jeito de se fazer
        faturamento = faturamento + valor_22
    else:
        faturamento = faturamento + valor_23
    print(f'Variação de {mes}: {var_percentual:.1%}')
# TODO: colocar o print que apaguei