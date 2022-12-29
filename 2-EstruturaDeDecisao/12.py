'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para
o Sindicato e que o FGTS corresponde a 11% do salário Bruto, mas não é descontado (é a empresa que deposita). O salário Líquido corresponde ao salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
salário Bruto até 900 (inclusive) - isento
salário Bruto até 1500 (inclusive) - desconto de 5%
salário Bruto até 2500 (inclusive) - desconto de 10%
salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações
'''

valor = 8#float(input('Insira o quanto você ganha por hora: '))
horas = 500#float(input('Insira a quantidade de horas trabalhadas no mês: '))

salario = valor*horas

if salario <= 900:
    IR = 0
elif salario <= 1500:
    IR = 0.05
elif salario <= 2500:
    IR = 0.10
elif salario >  2500:
    IR = 0.20

porcentagem = int(IR*100)
INSS = salario*0.10
FGTS = salario*0.11
IR = salario*IR

print(
f'''+ salario_bruto        : R$ {salario:.2f}
- IR ({porcentagem}%)             : R$ {IR:.2f}
- INSS (10%)           : R$ {INSS:.2f}
- FGTS (11%)           : R$ {FGTS:.2f}
- Total de descontos   : R$ {(IR+INSS+FGTS):.2f}
= salario Liquido      : R$ {salario-(IR+INSS+FGTS)}
''')