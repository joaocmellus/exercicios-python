'''Faça um Programa pue peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

data = input('Insira uma data no formato dd/mm/aaaa: ')

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

if mes >= 1 and mes <= 12:
    if mes in (1,3,5,7,8,10,12):
        if dia >= 1 and dia <= 31:
            print('A data está correta!')
        else:
            print('A dia está incorreto!')
    elif mes in (4, 6, 9, 11):
        if dia >= 1 and dia <= 30:
            print('A data está correta!')
        else:
            print('A dia está incorreto!')
    else:
        if ano%4 == 0:
            if dia >= 1 and dia <= 29:
                print('A data está correta!')
            else:
                print('A dia está incorreto!')
        else:
            if dia >= 1 and dia <= 28:
                print('A data está correta!')
            else:
                print('A dia está incorreto!')
else:
    print('O mês está incorreto!')