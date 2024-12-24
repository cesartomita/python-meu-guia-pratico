# O uso de Type Hint ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis.

# sem type hint

numero = 123
texto = 'Hello World!'
real = 999.99
ativo = True

# com type hint

numero: int = 123
texto: str = 'Hello World!'
real: float = 999.99
ativo: bool = True

# função sem type hint

def endereco_completo(rua, numero):
    print(f'Rua: {rua} - Número: {numero}')

# função com type hint

def endereco_completo(rua: str, numero: int):
    print(f'Rua: {rua} - Número: {numero}')