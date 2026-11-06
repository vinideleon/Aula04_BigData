#faça um algoritmo que verifique se um cliente de uma loja tem direito a um brinde. O programa deve pedir o valor total
#da compra e perguntar se o cliente é cadastrado no programa de fidelidade. o cliente ganha o brinde, se atender a pelo
#menos uma destas condições: Ter feito uma compra maior que R$ 100,00 ou ser cliente frequente.
#use o operador or, pois basta uma das condições ser verdadeira. Se o cliente tiver direito, mostre
#'' cliente tem direito a um brinde!'' caso contrario, mostre "sem brinde desta vez"

compra = float(input('valor da compra: '))
cliente_frequente = input('programa de fidelidade? [S/N]: ').lower()[0]

if compra > 100 or cliente_frequente == ('s'):
    print('Recebe o brinde')
else:
    print('sem brinde')