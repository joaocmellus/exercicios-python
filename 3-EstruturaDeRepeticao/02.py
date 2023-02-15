'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações'''

while True:
	usuario = input('Insira seu nome de usuário: ')
	senha = input('Insira sua Senha: ')
	if usuario == senha:
		print('Seu nome de usuário não pode ser igual à senha!')
		continue
	else:
		print('Dados aceitos!')
		break