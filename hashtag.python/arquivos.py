# Abrindo arquivos txt, csl,html

# With abre & já fecha os arquivos automaticamente

# with open('vendas.txt', 'w') # 'w' - edita as coisas dentro do arquivo
with open('vendas.txt', 'r') as arquivo: # 'r' jeito de ler o arquivo
# TRATANDO A STRING DO ARQUIVO

# fazer o que quiser com o arquivo
#infos = arquivo.read() # read ler as informações do arquivo escolhido
    infos = arquivo.readlines() # readlines - da as informações em lista python
vendas_totais = 0
for item in infos: # variavel item pegando o item da lista em Python
    # 'André, 300\n'
    #replace troca old pelo new
    item = item.replace('\n', '') # removendo a string \n por espaço vazio
    item = item.replace(' ', '') # remover espaço vazio no começo da posição da lista
    resultado = item.split(',') # split separa por posição na lista
    valor = resultado[1] # peganndo o valor na posição da lista
    valor = float(valor)
    vendas_totais = vendas_totais + valor

print(f'Vendas totais da lista R$ {vendas_totais:.2f}')


