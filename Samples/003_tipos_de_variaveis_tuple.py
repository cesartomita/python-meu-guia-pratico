# tuple - Coleções ordenadas de itens, mas ao contrário das listas, tuplas são imutáveis.
tupla_1 = ('a', 'b', 'c') 
tupla_2 = ('a', 2, True) 

print('Tipo da variável tupla_1:',type(tupla_1))
print('Tipo da variável tupla_2:',type(tupla_2))

# tupla com um único elemento
tupla_unico = ('a',)
print('Tipo da variável tupla_unico:',type(tupla_unico))

# tupla sem ',' não é uma tupla
tupla_nao_unico = ('a')
print('Tipo da variável tupla_nao_unico:',type(tupla_nao_unico))

# métodos de tuplas
tupla_metodo = ('a', 'b', 'c', 'a', 'd', 'a')

# count()
print(tupla_metodo.count('a'))

# index()
print(tupla_metodo.index('d'))

# desempacotando tupla
tupla_zip = (10, 20, 30)
a, b, c = tupla_zip
print(a)
print(b)
print(c)

# desempacotando tupla usando *
tupla_zip = (10, 20, 30, 40, 50, 60)
a, b, *c = tupla_zip
print(a)
print(b)
print(c)