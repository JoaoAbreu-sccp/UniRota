from functions import GeralDef, screen
from time import sleep

posicao_tipo = None  

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
        sleep(2)
        screen.clear()

    if opc == 3:
        break

if posicao_tipo is not None:

    if linhas[posicao_tipo] == "administrador":
        print("Adm entrou")

    if linhas[posicao_tipo] == "aluno":
        print("Aluno entrou")

    if linhas[posicao_tipo] == "motorista":
        print("motorista entrou")

        while True:
            screen.clear()
            print(f"Bem vindo, {linhas[posicao_senha+1]}")
            screen.menuMOT()
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
                print("Rota")
                print()
                with open("rota.txt") as arquivo:
                    arq = arquivo.read().splitlines()

                while True:
                    print(f"{'#':<3} | {'Check':<11} | {'Ponto de Parada':<30} | {'Endereço':<40}")
                    print("-" * 140)
                    
                    for i in range(0, len(arq), 3):
                        ponto = arq[i + 1].strip()
                        end = arq[i + 2]
                        check = arq[i].strip()
                    
                        print(f"{i // 3 + 1:<3} | {check:<11} | {ponto:<30} | {end:<40}")
                        print("-" * 140)

                    print()
                    
                    print("[1]: Dar Check\n[2]: Remover Check\n[3]: Sair")
                    print("=" * 50)
                    opcao = int(input("opção = "))
                    if opcao == 1:
                        print("=" * 50)
                        check_novo = int(input("Digite o número do ponto para dar check: "))
                        print("=" * 50)
                        comfirm = input("Tem certeza? [s/n] ")
                        if comfirm == "s":
                            arq[(check_novo - 1) * 3] = "True"
                            print("\nRota atualizada com sucesso")
                    
                    elif opcao == 2:
                        print("=" * 50)
                        check_novo = int(input("Digite o número do ponto para remover o check: "))
                        print("=" * 50)
                        comfirm = input("Tem certeza? [s/n] ")
                        if comfirm == "s":
                            arq[(check_novo - 1) * 3] = "False"
                            print("\nRota atualizada com sucesso")

                    elif opcao == 3:
                        sleep(0.5)
                        screen.clear()
                        break
                    
                    else:
                        print("Erro! Tente novamente. ): ")

                    with open("rota.txt", "w") as rota:
                        rota.write("\n".join(arq))


                    opc = input("\nDigite [s] para atualizar novamente:  ")
                    if opc == "s":
                        sleep(0.5)
                        screen.clear()
                    else:
                        break

                opc = int(input("\nDigite [1] para voltar:  "))
                sleep(0.5)
                screen.clear()
                    

            elif opc == 3:
                while True:
                    screen.clear()
                    print('''
            [1]: Criar Aviso
            [2]: Visualizar Avisos
            [3]: Voltar''')
                    opc = int(input("opc = "))
                    if opc == 1:
                        GeralDef.CreateNotice()
                    elif opc == 2:
                        avisos = open("avisos.txt", "r", encoding="utf-8")
                        linhasavisos = avisos.read().splitlines()
                        avisos.close()
                        screen.clear()
                        for aviso in linhasavisos:
                            print(aviso)
                        voltar = str(input("\nDigite [1] para voltar: "))
                    elif opc == 3:
                        break
                    else:
                        screen.clear()
                        print("Selecione uma opção valida...")
                        sleep(2)

            elif opc == 4:
                screen.clear()
                break

            else:
                print("Opção inválida :(")
                print("Tente novamente")