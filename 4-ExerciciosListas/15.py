'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada 
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:'''

num = []

while True:
	ins = int(input('Insira um número: '))
	if ins < 0:
		break
	else:
		num.append(ins)

# Mostre a quantidade de valores que foram lidos;
print(f'Foram lidos: {len(num)} números')

# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print('Todos os números:', num)

# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
num.reverse()
print('Ordem inversa:', num)

# Calcule e mostre a soma dos valores;
print('Soma:', sum(num))

# Calcule e mostre a média dos valores;
print('Média:', sum(num)/len(num))

# Calcule e mostre a quantidade de valores acima da média calculada;
x = 0
acima = []
abaixo = []
for i in num:
	if i > sum(num)/len(num):
		acima.append(i)
	if i < 7:
		abaixo.append(i)
print('Quantidade de valores acima da média:', len(acima))

# Calcule e mostre a quantidade de valores abaixo de sete;
print('Quantidade de valores abaixo de 7:', len(abaixo))

# Encerre o programa com uma mensagem
print('Mensagem bonitinha <3')