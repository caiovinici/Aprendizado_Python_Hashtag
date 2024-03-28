# Bibliotecas OS & REQUESTS - Modulos Python

import os # permite acessar as pastas do computador
arquivos = os.listdir() # listdir - lista tudo que está na pasta
print(arquivos)

# mover arquivos/pastas de local

# rename(arquivo desejado, destino de pasta/nome do arquivo
os.rename( 'vendas.txt', 'arquivos_vendas/vendas.txt')


# Organizando item dentro de pastas especificas
import os
lista_arquivos = os.listdir('arquivos_vendas') # listando itens da pasta
print(lista_arquivos)

for nome_arquivo in lista_arquivos: # pegando nome do item da lista no arquivo
     if 'txt' in nome_arquivo: # procurando a string TXT no nome do arquivo
         if '22' in nome_arquivo: # procura a string 22 no nome do arquivo
             os.rename(f'arquivos_vendas/{nome_arquivo}', f'arquivos_vendas/22/{nome_arquivo}')
         elif '23' in nome_arquivo:
             os.rename(f'arquivos_vendas/{nome_arquivo}', f'arquivos_vendas/23/{nome_arquivo}')


# Requests - consulta informações da internet
import requests

# pegando cotação do dolar online
link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

reposta = requests.get(link) # requisição requests / pegando informação do Link
# formato json
dic_reposta = reposta.json() # json transforma em um dicionario em Python a informação do Link
print(dic_reposta)
# {'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '4.938', 'low': '4.8602', 'varBid': '-0.0219', 'pctChange': '-0.45', 'bid': '4.8743', 'ask': '4.8755', 'timestamp': '1704488400', 'create_date': '2024-01-05 18:00:00'}, 'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '5.345', 'low': '5.345', 'varBid': '0', 'pctChange': '0', 'bid': '5.32', 'ask': '5.37', 'timestamp': '1704669136', 'create_date': '2024-01-07 20:12:16'}, 'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '218765', 'low': '214939', 'varBid': '350', 'pctChange': '0.16', 'bid': '216500', 'ask': '216604', 'timestamp': '1704669111', 'create_date': '2024-01-07 20:11:51'}}
print('=='*20)
cotacao_dolar = dic_reposta['USDBRL'] # pegando posicao da string no dicionario

print(f'Cotação do Dólar online R$ {cotacao_dolar['bid']}') # pegando a chave do dicionario []