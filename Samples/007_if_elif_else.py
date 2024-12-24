# exemplo 1
numero = int(input('Digite um número: '))

if numero <= 10:
    print('Seu número é menor ou igual a 10')
elif numero > 10 and numero <= 50:
    print('Seu número está entre 11 e 50')
else:
    print('Seu número é maior que 51')

# exemplo 2
lista_nome = ['João', 'Maria', 'Ana']
nome = 'Carlos'

if nome in lista_nome:
    print('Tem')
else:
    print('Não tem')