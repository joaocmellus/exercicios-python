import random

def sortear_numero() -> int:
    while True:
        min = input('Insira um valor mínimo inteiro: ')
        if not is_valid(min):
            print('O valor precisar ser um número inteiro\n')
        else:
            break    
    while True:
        max = input('Insira um valor máximo inteiro: ')
        if not is_valid(max):
            print('O valor precisar ser um número inteiro\n')
        else:
            break

    return random.randint(int(min), int(max))

def receber_palpite() -> int:
    while True:
        palpite = input('Insira seu palpite: ')
        if is_valid(palpite):
            return int(palpite)
        else:
            print('O palpite precisa ser um númeor inteiro!\n')

def is_valid(value:str) -> bool:
    if not value.isdigit():
        return
    if not float(value).is_integer():
        return
    return True

def main():
    numero = sortear_numero()
    while True:
        palpite = receber_palpite()
        if palpite == numero:
            print('Você acertou, parabéns!\n')
            break
        elif palpite > numero:
            print(palpite, 'é maior que o número secreto. Tente de novo.\n')
        else:
            print(palpite, 'é menor que o número secreto. Tente de novo.\n')

while True:
    main()
    r = input('Deseja jogar novamente? (s/n)').lower()
    if r in ('s', 'sim'):
        continue
    elif r in ('n', 'não', 'nao'):
        print('Obrigado por jogar!')
        break
    else:
        print('Resposta não esperada. Finalizando jogo!')
        print('Obrigado por jogar!')
        break