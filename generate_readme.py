import os


readme_content = """
# Python - Meu guia prático

Meu objetivo com este repositório é compartilhar os conhecimentos que adquiri sobre a linguagem Python. Deixo aqui alguns scripts simples, práticos e acessíveis, pensando em facilitar o aprendizado de quem está começando nessa linguagem.

### Clone o repositório:

`git clone https://github.com/cesartomita/javascript-meu-guia-pratico.git`

### Executando um arquivo:

Sintaxe do comando para executar:

`python <nome-do-arquivo.py>`

Exemplo de como executar o aquivo "hello_world.py", dentro do diretório "00 - Imprimindo Hello World":

`python '.\\00 - Imprimindo Hello World\\hello_world.py'`

Observação: Caso não tenha o Python instalado, clique [aqui](https://www.python.org/downloads/).
"""

def generate_readme(dir_path, readme_content, ignore_folders=None):
    if ignore_folders is None:
        ignore_folders = ['node_modules', '.git', '.bin']

    def read_directory(directory):
        nonlocal readme_content  # Permite modificar readme_content dentro desta função
        
        folders = []
        files = []

        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)

            if os.path.basename(item) in ignore_folders:
                continue

            if os.path.isdir(item_path):
                folders.append(item)
                read_directory(item_path)
            elif os.path.isfile(item_path):
                files.append(item)

        relative_dir = os.path.relpath(directory, dir_path).replace('\\', '/')
        if relative_dir == '.':
            relative_dir = ''

        if folders:
            readme_content += f"## {os.path.basename(directory)}\n\n"
            for folder in folders:
                folder_path = os.path.join(relative_dir, folder).replace('\\', '/')
                folder_path = folder_path.replace(' ', '%20')
                readme_content += f"- [{folder}]({folder_path}/)\n"

        if files:
            if not folders:
                readme_content += f"## {os.path.basename(directory)}\n\n"
            for file in files:
                file_path = os.path.join(relative_dir, file).replace('\\', '/')
                file_path = file_path.replace(' ', '%20')
                file_name_without_ext = os.path.splitext(file)[0]
                readme_content += f"- [{file_name_without_ext}]({file_path})\n"

    read_directory(dir_path)

    with open(os.path.join(dir_path, 'README.md'), 'w', encoding='utf-8') as readme_file:
        readme_file.write(readme_content)

    print('README.md gerado com sucesso!')

# Lista de pastas a serem ignoradas
ignored_folders = ['node_modules', '.git', '.bin']

# Chama a função passando o diretório atual e a lista de pastas a ignorar
generate_readme('./', readme_content, ignored_folders)
