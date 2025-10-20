from functions import loginverify, screen
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
            loginverify.PasswordReset(email)
        else:
            print("Insira um email válido")
        sleep(2)
        screen.clear()

    if opc == 3:
        break
if linhas[posicao_tipo] == "administrador":
    while True:
        screen.clear()
        print(f"Bem vindo, {linhas[posicao_senha+1]}")
        screen.menuADM()
        opc = int(input("opc = "))
        if opc == 1:
            screen.clear()
            listaalunos = open("listaalunos.txt")
            linhasalunos = listaalunos.read().splitlines()
            listaalunos.close()
            print("Lista de Alunos:")
            print(f"{'#':3}{'Nome':21}{'Instituição':21}  {'P. Embarque':21}  {'P. Desembarque':21}  {'Conf. Ida':21}  {'Conf. Volta':21}")
            index = 0
            for c, info in enumerate(linhasalunos):
                if c % 7 == 0 or c == 0:
                    if info != "":
                        index += 1
                        print(f"{index}. {info:18}", end=' | ')
                    else:
                        print()
                else:
                    if info != "":
                        print(f"{info:20}", end=' | ')
                    else:
                        print()
            opc = int(input("\nDigite [1] para voltar:  "))
            sleep(0.5)
            screen.clear()
        elif opc == 2:
            screen.clear()
            print("editar uni")
        elif opc == 3:
            screen.clear()
            print("editar aluno")
        elif opc == 4:
            screen.clear()
            print("acompanhar rota")
        elif opc == 5:
            screen.clear()
            print("adicionar aviso")
        elif opc == 6:
            break
        else:
            screen.clear()
            print("Selecione uma opção valida...")
            sleep(2)


if linhas[posicao_tipo] == "aluno":
    print("Aluno entrou")

if linhas[posicao_tipo] == "motorista":
    print("motorista entrou")