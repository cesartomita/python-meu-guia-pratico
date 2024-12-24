alunos = {}

def cria_aluno():

    nome = str(input('Digite o nome do aluno: '))
    if nome in alunos:
        idade = int(input('Digite a idade do aluno: '))
        print(f'Aluno {nome} atualizado com sucesso!')
    else:
        idade = int(input('Digite a idade do aluno: '))
        alunos[nome] = {'idade': idade}
        print(f'Aluno {nome} criado com sucesso!')

def busca_aluno():

    nome = str(input('Digite o nome que deseja buscar: '))
    if nome in alunos:
        print(f'Nome: {nome}')
        print(f'Idade: {alunos[nome]['idade']}')
    else:
        print('Nenhum aluno encontrado!')

def lista_aluno():

    if not alunos:
        print('Nenhum aluno cadastrado!')
    else:
        print(alunos)

def menu():

    while True:

        print('Menu:')
        print('1 - Criar aluno')
        print('2 - Buscar aluno')
        print('3 - Listar alunos')
        print('0 - Sair')
    
        escolha = int(input('Digite a opção que deseja: '))

        if escolha == 1:
            cria_aluno()
        elif escolha == 2:
            busca_aluno()
        elif escolha == 3:
            lista_aluno()
        elif escolha == 0:
            break
        else:
            print('Opção inválida!')

menu()