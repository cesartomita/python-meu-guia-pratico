# list
minha_lista_1 = [1, 2, 3, 4, 5]
minha_lista_2 = ['a', 'b', 'c', 'd', 'e']
minha_lista_3 = [1, 'b', 'c', 15.50, '999']

print('list')
print('Tipo da variável minha_lista_1:',type(minha_lista_1))
print('Tipo da variável minha_lista_2:',type(minha_lista_2))
print('Tipo da variável minha_lista_3:',type(minha_lista_3))

# inserindo dados

# exemplo de lista
lista = [1, 2, 3]
print(lista)

# adicionando item no final da lista
lista.append(4)
print(lista)

# inserindo item em uma posição específica
# inserindo item 'meu_item' na posição 3 da lista
lista.insert(3, 'meu_item')
print(lista)

# inserindo múltiplos itens no final da lista
lista.extend(['a', 'b', 'c'])
print(lista)

# apagando dados

# exemplo de lista
lista = ['a', 'b', 'c', 'a', 'd', 'e', 'f']
print(lista)

# removendo o primeiro item com o valor 'a'
lista.remove('a')
print(lista)

# removendo item na posição 2
lista.pop(2)
print(lista)

# removendo o último item
lista.pop()
print(lista)

# removendo o item na posição 1 usando del
del lista[1]
print(lista)

# removendo todos os itens
lista.clear()
print(lista)

# atualizando dados

# exemplo de lista
lista = ['Bob', 'Jon', 'Ana']
print(lista)

# atualizar o valor na posição 2
lista[2] = 'Ana Smith'
print(lista)

# atualizando múltiplos itens
lista[0:2] = ['Bob Smith', 'Jon Smith']
print(lista)