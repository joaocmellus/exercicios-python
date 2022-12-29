'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)'''

tamanho = float(input('Tamanho do arquivo (MB):\n'))
velocidade = float(input('Velocidadedo link da Internet(MBps):\n'))

tempo = tamanho/velocidade

minutos = tempo/60

print(f'O seu download estará concluído daqui a {int(minutos)} minutos')