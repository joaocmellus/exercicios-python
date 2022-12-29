'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = 1500#float(input('Insira o salário atual: '))

if salario <= 280.00:
    aumento = 0.20
elif salario > 280.00:
    aumento = 0.15
elif salario > 700.00:
    aumento = 0.10
elif salario > 1500.00:
    aumento = 0.05

ajuste = salario*aumento
salario_novo = salario+ajuste
aumento = int(aumento*100)

print(f'''
: Salário antes do reajuste:       R${salario:.2f}
: Percentual de aumento aplicado:  {aumento}%
+ Valor do aumento:                R${ajuste:.2f}

= Novo salário após o aumento:     R${salario_novo:.2f}
''')