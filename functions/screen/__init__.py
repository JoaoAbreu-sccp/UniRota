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
[4]: Editar motoristas
[5]: Acompanhar Rota
[6]: Adicionar Aviso
[7]: Sua conta
[0]: Sair''')
    
def menuUniversidades():
    print('''
==== GERENCIAR UNIVERSIDADES ====
[1]: Cadastrar Universidade
[2]: Listar Universidades
[3]: Editar Universidade
[4]: Excluir Universidade
[0]: Voltar''')

def menuADM_sua_conta():
    print('''-------------------------
        Sua conta  
-------------------------
          
[1]: Informações pessoais
[2]: Credênciais
[0]: Voltar
          ''')
    
    opc=int(input("Digite: "))
    return opc

def editar_usuário_menu(tipo_de_usuário):
    print(f"""-------------------------
    Editar {tipo_de_usuário}  
-------------------------          
[1]: adicionar {tipo_de_usuário}
[2]: remover {tipo_de_usuário}
[3]: editar {tipo_de_usuário}
[0]: Voltar
""")
    opc=int(input("Por favor selecione uma opção: "))
    return opc
