"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""

completo = False
while not completo:
	nome = input('Insira o nome: ')
	if not len(nome) > 3:
		print('Nome inválido!\n')
		continue

	idade = input('Insira a idade: ')
	if idade.isdigit():
		idade = int(idade)
		if idade < 1 or idade > 150:
			print('Idade inválida!\n')		
			continue
	else:
		print('Idade inválida!\n')
		continue

	salario = input('Insira o salário: ')
	if salario.isdigit():
		salario = float(salario)
		if not salario > 0:
			print('Salário inválido!\n')
			continue	
	else:
		print('Salário inválido!\n')
		continue

	sexo = input('Insira o sexo(f/m): ').lower()
	if sexo not in ('f','m'):
		print('Sexo inválido!\n')
		continue

	estado_civil = input('Insira seu Estado Civil(s/c/v/d): ')
	if estado_civil not in ('s', 'c', 'v', 'd'):
		print('Estado civil inválido!\n')
		continue
	completo = True