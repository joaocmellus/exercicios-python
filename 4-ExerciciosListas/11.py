# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

gA = []
gB = []
gC = []

for i in range(10):
	gA.append(int(input('Insira um número para o grupo A: ')))
print()
for i in range(10):
	gB.append(int(input('Insira um número para o grupo B: ')))
print()
for i in range(10):
	gC.append(int(input('Insira um número para o grupo B: ')))

inter = gA + gB + gC

print(gA)
print(gB)
print(gC)
print(inter)