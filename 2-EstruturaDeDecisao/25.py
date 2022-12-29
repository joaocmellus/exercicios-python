'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''

perguntas = ['Você telefonou para a vítima? (s/n): ', 'Você esteve no local do crime? (s/n): ',
'Você mora perto da vítima? (s/n): ', 'Você devia para a vítima? (s/n): ', 
'Já trabalhou com a vítima? (s/n): ']
respostas = []

for i in perguntas:
	respostas.append(input(i).lower()[0])

suspeita = respostas.count('s')

if suspeita < 2:
	print('Inocente')
elif suspeita == 2:
	print('Suspeita')
elif suspeita <= 4:
	print('Cúmplice')
else:
	print('Assassino')
input()