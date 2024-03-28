def calcular_imposto2(preco, ir=0.275, csll=0.35, iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll, imposto_iss # retornando + de 1 variavel

respota = calcular_imposto2(1000)
print(respota) # Tuplas = sem editação

ir, csll, iss = calcular_imposto2(1000)
print(ir, csll, iss, sep='\n') # sep separador
print('=='*20)


tamanho_tela = (1920, 1080) # definindo tupla
