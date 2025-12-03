def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('''
Bem vindo ao Unirota!

[1]: Fazer Login
[2]: Redefinir Senha
[3]: Sair''')

def menuADM():
    print('''
[1]: Lista de Alunos
[2]: Editar Universidades
[3]: Editar Alunos
[4]: Acompanhar Rota
[5]: Adicionar Aviso
[6]: Sair''')