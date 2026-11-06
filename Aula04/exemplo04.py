#faça um programa que simule o login em um sistema. o programa deve pedir ao usuario o nome de usuario e a senha
#acesso so sera liberado somente se as duas informações estiverem corretas:
#nome de usuario: Admin. Senha deve ser: 1234.
#se o login for valido, mostre ''login realizado com sucesso.'' caso contrario, mostre ''usuario ou senha incorretos.''

nome = input('nome do usuario: ')
senha = input('digite a sua senha: ')

if nome == 'admin' and senha == '1234':
    print('login realizado com sucesso!!! ')

else:
    print('usuario ou senha incorretos!!! ')
    