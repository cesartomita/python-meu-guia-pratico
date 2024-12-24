# Biblioteca nativa do Python
import csv

# Caminho do arquivo CSV
caminho_arquivo = './data/iris.csv'

# Inicializa uma lista vazia para armazenar os dados
dados_csv = []

# Usa o gerenciador de contexto `with` para abrir o arquivo
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    
    # Itera sobre as linhas do arquivo CSV
    leitor_csv = csv.DictReader(arquivo)

    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        dados_csv.append(linha)

# Mostra todos os dados lidos do CSV
for registro in dados_csv:
    print(registro)

# Exemplos de como mostrar os dados lidos
print(dados_csv[1])
print(dados_csv[3]['Id'])
print(dados_csv[5]['Species'])