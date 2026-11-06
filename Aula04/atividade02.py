# uma loja deseja premiar seus vendedores de acordo com o valor total de suas vendas.
# o valor do bonus vai ser acrescentado ao salario base do vendedor
# vendas iguais ou superiores a R$ 1.000,00: bonus de R$ 150,00
# vendas iguais ou superiores a R$ 500,00: bonus de R$ 75,00
# vendas inferiores a R$ 500,00: sem bonus
# o programa deverá calcular o valor do bonus, soma-lo ao salario e apresentar o valor total com o bonus.

salario = float(input('qual é o seu salario? '))
venda = float(input('qual é o valor total da sua venda? '))

if venda >= 1000:
    bonus = 150
    valor_final = salario + bonus
    print(f'parabens o seu bonus é de {bonus}. \nE o seu salario total é de {valor_final:.2f}')

elif venda >= 500:
    bonus = 75
    valor_final = salario + bonus
    print(f'parabens o seu bonus é de {bonus}. \nE o seu salario total é de {valor_final:.2f}')

else:
    print(f'você não possui bonus. \no seu valor final é {venda:.2f}')

