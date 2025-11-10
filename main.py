from functions import GeralDef, screen
from time import sleep


while True:
    logins = open("logins.txt")
    linhas = logins.read().splitlines()
    logins.close()

    
    screen.menu()
    opc = int(input("opc = "))
    screen.clear()

    if opc == 1:
        email = input("Digite o Email de Login: ").strip()
        senha = input("Digite a senha de acesso: ").strip()
        if email in linhas:
            posicao_senha = linhas.index(email)+1
            if linhas[posicao_senha] == senha:
                posicao_tipo = linhas.index(email)-1
                print(f"Entrando como {linhas[posicao_tipo]}")
                break
            else:
                print("Email ou senha incorretos...")
                sleep(2)
                screen.clear()
        else:
            print("Email ou senha incorretos...")
            sleep(2)
            screen.clear()

    if opc == 2:
        email = input("Digite o email cadastrado: ")
        if email.endswith("@gmail.com"):
            GeralDef.PasswordReset(email)
        else:
            print("Insira um email válido")
        sleep(1)
        screen.clear()

    if opc == 3:
        break
if linhas[posicao_tipo] == "administrador":
    print("Admin logado!")
    sleep(2)

    from ADM_universidades import (
        cadastrar_universidade,
        listar_universidades,
        editar_universidade,
        excluir_universidade
    )

    while True:
        screen.clear()
        screen.menuADM()
        opc = input("Opção: ")

        if opc == "2":  # Editar universidades
            while True:
                screen.clear()
                screen.menuUniversidades()
                subopc = input("Opção: ")

                if subopc == "1":
                    cadastrar_universidade()
                elif subopc == "2":
                    listar_universidades()
                elif subopc == "3":
                    editar_universidade()
                elif subopc == "4":
                    excluir_universidade()
                elif subopc == "0":
                    break
                else:
                    print("Opção inválida!")
                    sleep(1)

        elif opc == "6":  # Sair do painel ADM
            print("Saindo do painel do administrador...")
            sleep(1)
            break
        else:
            print("Função ainda não implementada ou opção inválida.")
            sleep(1)
            break

if linhas[posicao_tipo] == "aluno":
    print("Aluno entrou")

if linhas[posicao_tipo] == "motorista":
    print("motorista entrou")

    