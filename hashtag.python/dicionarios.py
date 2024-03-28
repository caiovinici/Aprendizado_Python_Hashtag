precos = [1500, 1000, 800, 2000]
produtos = ['celular', 'câmera', 'fone de ouvido', 'monitor']


dic_precos = {'celular': 1500, 'câmera': 1000, # dicionarios usa {}
              'fone de ouvido': 800, 'monitor': 2000}

# pegar item no dicionario
precos_celular = dic_precos['celular']
print(precos_celular)


# editando preço do dicionario
dic_precos['celular'] = 2000
print(dic_precos)


# adicionar item no dicionario
dic_precos['iphone'] = 4500
print(dic_precos)


# deletador valor do dicionario
dic_precos.pop('iphone')
print(dic_precos)


# tamanho do dicionario
print(len(dic_precos))


# pegando nome & valor do produto
print(dic_precos.keys())
print(dic_precos.values())
