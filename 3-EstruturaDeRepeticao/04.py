'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% 
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e 
escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas
as taxas de crescimento.'''

país_a = 80000 
país_b = 200000
ano = 0

while paísB > paísA:
	ano += 1
	país_a += (país_a * 0.03)
	país_b += (país_b * 0.015)
	print(f'Ano {ano}')