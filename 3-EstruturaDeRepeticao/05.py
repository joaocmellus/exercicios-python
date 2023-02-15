"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação."""


país_a = int(input('Insira a população do País A: '))
aumento_anual_a = float(input('Insira o aumento anual da população do país A: '))
país_b = int(input('Insira a população do País B: '))
aumento_anual_b = float(input('Insira o aumento anual da população do país B: '))
ano = 0

if	país_a > país_b:
	print('A população do País A já é maior que a população do País B!')

while país_b > país_a:
	ano += 1
	país_a += (país_a * aumento_anual_a)
	país_b += (país_b * aumento_anual_b)
	print(f'Ano {ano}')
