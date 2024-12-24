# exemplo 1
numero = 1
total = 0

while numero < 10:
    total = numero + 1
    numero = numero + 1
print(total)

# exemplo 2
while True:
    senha = str(input('Digite a senha: '))
    if senha == '123456':
        break
    print('Senha incorreta!')

# exemplo 3
letras = ['a', 'b', 'c']
while letras:
    letra = letras.pop()
    print(f'Removendo: {letra}')