#perguntar ao usuario/a o valor da compra. caso o valor seja maior que R$250.00: aplicar um desconto de 16%
#exibir o valor final com o desconto aplicado. caso contrario exibir o valor original da compra(sem desconto).

valor = float(input('qual é o valor da compra? '))


if valor > 250.00:
    desconto = valor * 0.16
    valor_final = valor - desconto
    print(f'desconto de R$ {desconto:.2f}. \ntotal a pagar: R$ {valor_final:.2f}')
    

else:
    print(f'o valor da sua compra é: {valor:.2f}')

