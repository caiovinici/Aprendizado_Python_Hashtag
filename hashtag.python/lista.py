vendas = [100, 50, 130, 80, 120, 200] # criando listas []
#produtos = ['iphone', 'ipad', 'airpod']

#pega a posição do elementro dentro da lista - ex;0123456789
print(vendas[0])


# forma de sempre pegar o ultimo item da lista (da direita para esquerda)
#[-2] pega o penultimo da lista
print(vendas[-1])

total_vendas = sum(vendas)
print(total_vendas)


# len . contando quantos item tem dentro da lista []
quantidade = len(vendas)
print(quantidade)


# max|min . pega o valor maximo e minimo dentro da lista []
valor_max = max(vendas)
valor_min =  min(vendas)
print(valor_max, valor_min)


# .index descobre a posição do elemento na lista  ex; (130) <-
posicao = vendas.index(130)
print(posicao)


# [2:] forma de pega pedaço da lista
print(vendas[2:]) # pega posicao desejada da strin
print(vendas[:3]) # começa pela posição 0 da string


produtos = ['iphone', 'ipad', 'airpod']
precos = [4000, 8000, 2000]

# edita valor do item
print('iphone' in produtos) #. item q deseja procura IN local qe deseja procurar
precos[0] = 4500 # editando valores dentro da lista
novo_preco = precos[1] * 1.1 # aumentando preço com 10% dentro da lista
# precos[0] = precos[0] * 1.1 # aumentando o preço cm 10% dentro da lista
precos[1] = novo_preco
print(precos)


# usuario procurando produto na lista
produto_usuario = input('Digite o nome do produto:')
print(produto_usuario in produtos)


# inserindo novos produtos na lista
produtos.append('macbook') # sera inserido no fim da lista
precos.append(10000)
print(produtos)
print(precos)


# remover um item
produtos.remove('macbook')
precos.pop(-1) # remove com a posicao na lista
print(produtos)
print(precos)


# inserir um valor
produtos.insert(1, 'airpod') # posicao primeiro, dps item desejado
print(produtos) 


# contar valores
print(produtos.count('airpod'))


# ordenar lista
precos.sort() # ordem crescente / decrescente sort(reverse=True)
print(precos)
