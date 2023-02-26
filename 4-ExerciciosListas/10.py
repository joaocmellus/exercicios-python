# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

gA = []
gB = []

for i in range(10):
	gA.append(int(input('Insira um número para o grupo A: ')))
print()
for i in range(10):
	gB.append(int(input('Insira um número para o grupo B: ')))

inter = gA + gB

print(gA)
print(gB)
print(inter)