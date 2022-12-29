'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

print('''Informe seu sexo:
    F - Feminino
    M - Masculino''')
op = input().lower()

if op[0] == 'm':
    print('você é do sexo Masculino!')
elif op[0] == 'f':
    print('Você é do sexo Feminino!')
else:
    print('Opção inválida!')