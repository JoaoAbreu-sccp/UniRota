def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('''
Bem vindo ao Unirota!

[1]: Fazer Login
[2]: Redefinir Senha
[3]: Sair''')