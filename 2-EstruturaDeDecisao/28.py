'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                Até 5 Kg                Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do 
desconto e valor a pagar.
'''

print('Opções de carne:\n1 - Filé Duplo\n2 - Alcatra\n3 - Picanha')

op = int(input('Opção escolhida: '))
quantidade = float(input('Quantidade comprada: Kg '))

if op in (1,2,3,4): 
    if op == 1:
        op = 'Filé Duplo'
        if quantidade > 5:
            preco = quantidade * 5.80
        else:
            preco = quantidade * 4.90
    
    elif op == '2':
        op = 'Alcatra'
        if quantidade > 5:
            preco = quantidade * 6.80
        else:
            preco = quantidade * 5.90
    
    elif op == '3':
        op = 'Picanha'
        if quantidade > 5:
            preco = quantidade * 7.80
        else:
            preco = quantidade * 6.90   

    pagamento = int(input('Forma de pagamento:\n1 - Cartão Tabajara\n2 - Cartão Genérico\n'))
    if pagamento == 1:
        pagamento = "Cartão Tabajara"
        des = preco * 0.05
        preçoFinal = preco - des 

    else:
        pagamento = preçoFinal = preco
        pagamento = "Cartão Genérico"
        des = 0

    print(f'''Compra: {op}
Kg {quantidade:.2f}
Valor total: R${preco:.2f}
Forma de Pagamento: {pagamento}
Desconto: R${des:.2f}
Valor final: R${preçoFinal:.2f}''')

else:
    print('Opção Inválida!')