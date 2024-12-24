# exemplo

try:
    resultado = len(3)
    print(resultado)
except TypeError as e:
    print(e)
else:
    print('Entrou no else')
finally:
    print('Finalizado')

# # exemplo 2

try:
    result = (10 / 0)
    print(result)
except Exception as e:
    print(f'Error: {e}')
else:
    print('Entrou no else')
finally:
    print('Finalizado')


# exemplo 3

try:
    result = 5 + 5
except ZeroDivisionError:
    print ("a/b result in 0")
else:
    print (result)

