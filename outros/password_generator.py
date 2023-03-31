import random

class PasswordGenerator:
    def __init__(self):
        self.lower_char = [chr(i) for i in range(ord('a'), ord('z'))]
        self.upper_char = [chr(i) for i in range(ord('A'), ord('Z'))]
        self.numbers = [str(i) for i in range(10)]
        self.symbols = ['@', '#', '$', '%', '*', '&']
        
    def rand_lower_char(self)  -> str:
        return random.choice(self.lower_char)

    def rand_upper_char(self)  -> str:
        return random.choice(self.upper_char)

    def rand_number_char(self) -> str:
        return random.choice(self.numbers)

    def rand_symbol_char(self) -> str:
        return random.choice(self.symbols)

    def generate(
            self, size:int, lower_char=True, upper_char=True,
            number=True, symbol=True
        ) -> str:   
        """
        Retorna uma senha aleatória com o tamanho e o tipo de caracter
        definido pelo usuário.

        :param size: <int> número de caractéres da senha.
        """
        choices = [
            self.rand_lower_char,  self.rand_upper_char,
            self.rand_number_char, self.rand_symbol_char
        ]
        weights = [0, 0, 0, 0]

        if lower_char:
            weights[0] = 3.5 
        if upper_char:
            weights[1] = 3 
        if number:
            weights[2] = 2
        if symbol:
            weights[3] = 1.5
        
        password = ''
        for i in range(size):
            generator = random.choices(choices, weights)[0]
            password += generator()
        
        return password
    
    def custom_generate(
            self, lower_char=1, upper_char=0, 
            number_char=0, symbol_char=0
        ) -> str:
        """
        Retorna uma senha aleatória com o tamanho, tipo e quantidade de
        cada caracter definido pelo usuário.

        :param lower_char: <int> número de caracteres minúsculos
        :param upper_char: <int> número de caracteres maiúsculos
        :param number: <int> número de caracteres numéricos
        :param symbol: <int> número de caracteres especiais
        """
        quantities = [
            lower_char,  upper_char,
            number_char, symbol_char
        ]
        choices = [
            self.rand_lower_char,  self.rand_upper_char,
            self.rand_number_char, self.rand_symbol_char
        ]
        password = ''
        lenght = sum(quantities)
        while len(password) < lenght:
            rand = random.randint(0, len(quantities)-1)
            if quantities[rand] > 0:
                generator = choices[rand]
                password += generator()
                quantities[rand] -= 1
            else:
                del quantities[rand]
                del choices[rand]
        return password

def main():
    while True:
        # entrada cmd...
        break

if __name__ == '__main__':
    main()