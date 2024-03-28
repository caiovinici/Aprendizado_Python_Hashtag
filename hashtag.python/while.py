# Cadastro de produto

produtos = ['iphone', 'ipad', 'airpod']

# While forma de repetição == For
while True: # True é sempre verdadeiro
    novo_produto = str(input('Novo Produto: ')).strip().lower()
    print('=='*20)

    if 's' == novo_produto:
        print('Fim do programa')
        break # interrompe o while

    if novo_produto in produtos:
        print('Produto já cadastrado')
    else:
        print(f'Produto \033[4;32m{novo_produto}\033[m cadastrado com sucesso !')
        produtos.append(novo_produto) # append adiciona o produto na (lista informada)
    print(produtos)
    print('Digite (s) se desejar sair.')
    