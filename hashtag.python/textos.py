faturamento = 1000
custo = 700
lucro = faturamento - custo
print(f'Faturamento: R${faturamento:.2f}, Custo: R${custo:.2f}, Lucro: R${lucro:.2f}')


email = 'EMAIL_falso@gmail.com'
        #01234567891011
print(email.lower()) # deixa as str tudo em minusculas
print(email.find('@')) # procura o que esta dentro do ('') cm a posicao

print(f'Posição da STR {email[11]}') # [] da a posicao da str
posicao = email.find('@')
servidor = email[posicao:] # pegando pedaco da str
print(servidor)

# Tamanho de um texto - len()
tamanho = len(email)
print(f'Tantos de caracteres {tamanho}')

# trocar um str pela outra
email_trocado = email.replace('gmail.com', 'hotmail.com')
print(email_trocado)

nome = 'Caio vinicius'
print(nome.capitalize()) # somente a primeira letra em maiuscula
print(nome.title()) # coloca a primeira letra de cada STR -> Caio Vinicius
