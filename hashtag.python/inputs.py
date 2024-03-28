# input - permiter o usuario digitar
#nome = input('Digite aqui seu e-mail: ')
#print(nome)

email = (str(input('Digite seu e-mail: '))).lower().strip()
posicao = email.find('@')
servidor = email[posicao:]
print(f'O servidor do e-mail é {servidor}') # pegando somente @gmail/@hotmail do e-mail

# pegar primeiro nome do usuario
nome_usuario = (str(input('\nNome completo: '))).capitalize().strip()
posicao_nome = nome_usuario.find(' ')
print(f'Seja bem - vindo(a) {nome_usuario[:posicao_nome]} seu cadastro está quase pronto...!')

# construir msg de sucesso de cadastro com o email
print(f'\nSeu cadastro foi feito com o e-mail {email}'.title())

# construir msg de link de confirmacao de email
print(f'Enviamos o código de confirmação no e-mail {email[0]}****{servidor}')
from time import sleep
sleep(1)
print(f'Cadastro feito com sucesso {nome_usuario[:posicao_nome]}')
