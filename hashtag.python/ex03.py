# Sistema de procura preço em Dicionario

dic_precos = {'celular': 1500, 'câmera': 1000, # dicionarios usa {}
              'fone de ouvido': 800, 'monitor': 2000}

produto_procurado = str(input('Nome do produto: ')).strip().lower()
print('===' * 10)

from time import sleep
sleep(1)

if produto_procurado in dic_precos:
    preco = dic_precos[produto_procurado]
    print(f'Produto: {produto_procurado} \nPreço: R${preco:.2f}')
else:
    print('Produto não encontrado, tente novamente!')
