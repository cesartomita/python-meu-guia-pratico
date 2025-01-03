# Tipos de variaveis

# int
x = 42
y = 123456
z = 0

print('int')
print('Tipo da variável x:',type(x))
print('Tipo da variável y:',type(x))
print('Tipo da variável z:',type(x))

# float
x = 1.75
y = 44.44
z = 0.00009

print('float')
print('Tipo da variável x:',type(x))
print('Tipo da variável y:',type(x))
print('Tipo da variável z:',type(x))

# str - string
x = 'Hello World!'
y = 'Test'
z = '123'

print('str')
print('Tipo da variável x:',type(x))
print('Tipo da variável y:',type(x))
print('Tipo da variável z:',type(x))

# bool - boolean
a = True
b = False

print('bool')
print('Tipo da variável a:',type(a))
print('Tipo da variável b:',type(b))

# bytes
x = b'Hello World'

print('bytes')
print(x)
print('Tipo da variável x:',type(x))

# Codificar uma string em bytes usando UTF-8
text = "Meu texto"
encoded = text.encode('utf-8')
print(encoded) # b'Meu texto'

# Decodificar bytes de volta para uma string
decoded = encoded.decode('utf-8')
print(decoded) # 'Meu texto'