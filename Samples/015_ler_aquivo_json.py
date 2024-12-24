import json

arquivo_json = './data/iris.json'

with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print(dados)
print(dados[1])
print(dados[3]['species'])