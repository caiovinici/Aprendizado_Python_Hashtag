# Sistema de consula de preços em Lista

precos = [1500, 1000, 800, 2000]
produtos = ['Celular', 'Câmera', 'Fone de ouvido', 'Monitor']
produto_procurado = str(input('Nome do produto: ')).capitalize().strip()
print('=#=' * 15)

from time import sleep
sleep(1)

if produto_procurado in produtos:
    posicao = produtos.index(produto_procurado) # pegando posicao do produto na lista
    preco = precos[posicao] # pegando o preço do produto na lista
    print(f'Produto: {produto_procurado} \nPreço R${preco:.2f}')
else:
    print('Produto não encontrado, tente novamente!')
