# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes

ins = input('Insira uma palavra: ')

consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

letras = []

for i in ins:
	if i in consoantes:
		letras.append(i)

print(f'{len(letras)} consoantes foram lidas')
print(letras)