'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                Até 5 Kg                 Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

frutas = { 
    'Maçãs':    [2.50, 2.20], 
    'Morangos': [1.80, 1.50]
}
quantidade = []
for i in frutas.keys():
    quantidade.append(float(input(f'Insira a quantidade de {i}: Kg ')))

precos = []
for i, j in enumerate(frutas.keys()):
    if quantidade[i] <= 5:
        precos.append(quantidade[i] * frutas[j][0])
    else:
        precos.append(quantidade[i] * frutas[j][1])

peso = sum(quantidade)
preco = sum(precos)

if preco > 25 or peso > 8:
    preco -= preco * 0.1

print(f'Preço total: R${preco:.2f}')