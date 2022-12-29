'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''

valor = float(input('Insira o salário recebido por hora: '))

horas = float(input('Insira as horas trabalhadas no mês: '))

bruto = valor * horas

IR = bruto * 0.11

INSS = bruto * 0.08

sindicato = bruto * 0.05

salário = bruto - IR - INSS - sindicato

print(f'''
+ Salário Bruto:    R${bruto:.2f}
- Imposto de Renda: R${IR:.2f}
- INSS:             R${INSS:.2f}
- Sindicato:        R${sindicato:.2f}

= Salário Líquido:  R${salário:.2f}'''
)