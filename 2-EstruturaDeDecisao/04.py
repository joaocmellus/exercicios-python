#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Insira uma letra:\n')

vogais = ['a','e','i','o','u']

consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ç']

if letra in vogais:
    print(f'{letra} é uma vogal!')
elif letra in consoantes:
    print(f'{letra} é uma consoante!')
else:
    print(f'{letra} não é uma letra!')