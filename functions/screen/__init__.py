def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('''-------------------------
  Bem vindo ao Unirota!  
-------------------------
          
[1]: Fazer Login
[2]: Redefinir Senha
[0]: Fechar''')


#ADMNISTRADOR

def menuADM():
    print('''-------------------------
    Menu Admnistrador   
-------------------------
          
[1]: Lista de Alunos
[2]: Gerenciar Universidades
[3]: Gerenciar Alunos
[4]: Gerenciar motoristas
[5]: Rota
[6]: Adicionar Aviso
[7]: Sua conta
[0]: Sair''')
    
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
[1]: visualizar {tipo_de_usuário}   
[2]: adicionar {tipo_de_usuário}
[3]: remover {tipo_de_usuário}
[4]: editar {tipo_de_usuário}
[0]: Voltar
""")
    opc=int(input("Por favor selecione uma opção: "))
    return opc

def menuUniversidades():
    print(f'''-------------------------
 GERENCIAR UNIVERSIDADES 
-------------------------
[1]: Cadastrar Universidade
[2]: Listar Universidades
[3]: Editar Universidade
[4]: Excluir Universidade
[0]: Voltar''')
    
def rota():
    print(f'''-------------------------
       Editar rota 
-------------------------
[1]: Acompanhar rota
[2]: Adicionar ponto
[3]: Remover ponto  
[0]: Voltar
''')
    opc=int(input("Por favor selecione uma opção: "))
    return opc

def menuAVISO():
    print(
                            """
-------------------------
     Adicionar Aviso 
-------------------------

[1]: Criar Aviso
[2]: Visualizar Avisos
[3]: Editar / Excluir Aviso
[0]: Voltar
""")
#ALUNO
def cabecalho(texto="página inicial"):
    print(f"------------------------------{texto}------------------------------")
    print()

def paginainicial():
    print('''
Bem vindo ao painel do aluno!

[1]: Confirmar Check-in
[2]: Cancelar Check-in          
[3]: Dados pessoais
[4]: Acompanhar rota
[5]: Visualizar Avisos          
[6]: Sair      
          ''')



#MOTORISTA
def menuMOT():
    print('''-------------------------
    Menu Motorista   
-------------------------
[1]: Lista de Alunos
[2]: Atualizar Rota
[3]: Adicionar Aviso
[4]: Sair''')

