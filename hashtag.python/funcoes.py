list_preco = [1500, 1000, 800, 3000]
total_imposto = 0 # acumulado

# Usando função def - declara e define uma função
def calcular_imposto(preco, aliquota1=0.2, aliquota2=0.15, aliquota3=0.1):
    # passar a vareavel dentro de ()
    if preco > 2000:
        imposto = preco * aliquota1 #0.2 - 20%
    elif preco > 1000:
        imposto = preco * aliquota2 #0.15 - 15%
    else:
        imposto = preco * aliquota3 #0.1 - 10%
    print(f'Preço {preco:.2f} --- Imposto {imposto:.2f}')
    return imposto
    # return sempre no fim de def, pra ter retorno da variavel de dentro da def

for preco in list_preco:
        imposto = calcular_imposto(preco, aliquota1=0.25) #alterando somente 1 aliquota
        total_imposto = total_imposto + imposto
print(f'Imposto total {total_imposto}')
print('=='*20)

# def se_inscrever(): # Função
#     print('Se inscreve no canal')
# for i in range(10):
#     se_inscrever()


def calcular_imposto2(preco, ir=0.275, csll=0.35, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss # retornando + de 1 variavel

respota = calcular_imposto2(1000)
print(respota) # Tuplas

