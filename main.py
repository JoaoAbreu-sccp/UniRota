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
                tipo_de_usuario=linhas[posicao_tipo]
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
                        
                csv_gerado = False

            while True:
                if not csv_gerado:
                    opc_1 = int(input('''\n[1]: Exportar para CSV\n[0]: Sair\n\nDigite: '''))
                else:
                    opc_1 = int(input("\n[0]: Sair\n\nDigite: "))

                if opc_1==1:
                    screen.clear()
                    print("Exportando...")
                    sleep(0.2)
                    with open("alunos_exportados.csv", "w", newline="", encoding="cp1252") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(["Nome", "Instituição", "P. Embarque", "P. Desembarque", "Conf. Ida", "Conf. Volta"])

                        for i in range(0, len(linhasalunos), 7):
                            bloco = linhasalunos[i:i+7]
                            if len(bloco) >= 6:
                                    writer.writerow(bloco[:6])

                        print("Exportado com sucesso para 'alunos_exportados.csv'!")
                        csv_gerado=True
                        sleep(1)
                        
                elif opc_1 == 0:
                    print("Saindo...")
                    sleep(0.5)
                    break

                else:
                    print("Opção inválida! Tente novamente.")
            sleep(0.5)

            opc = int(input("\nDigite [1] para voltar:  "))
            sleep(0.5)
            screen.clear()
        elif opc == 2:
            screen.clear()
            print("Adm entrou")         
        elif opc == 3:
            screen.clear()
            opc_1=screen.editar_usuário_menu("aluno")
            if opc_1==1:
                screen.clear()
                GeralDef.Adicionar_usuario("aluno")
            elif opc_1==2:
                GeralDef.Excluir_usuario('aluno')
            elif opc_1==3:
                GeralDef.Editar_usuário("aluno")
        
        elif opc == 4:
            screen.clear()
            opc_1=screen.editar_usuário_menu("motorista")
            if opc_1==1:
                GeralDef.Adicionar_usuario("motorista")
            elif opc_1==2:
                GeralDef.Excluir_usuario('motorista')
            elif opc_1==3:
                GeralDef.Editar_usuário("motorista")
                
        elif opc == 5:
            screen.clear()
            print("Acompanhar Rota")
            
        elif opc == 6:
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
        elif opc == 7:
            print("Saindo do painel do administrador...")
            sleep(1)
            
            break


        elif opc == 8:
            while True:
                screen.clear()
                opc_1=screen.menuADM_sua_conta()
                if opc_1==1:
                    GeralDef.Sua_conta(tipo_de_usuario)
                elif opc_1==2:
                    GeralDef.Credenciais(tipo_de_usuario)
                elif opc_1==0:
                    break
                else:
                    print("Por favor insira uma opção valida! ")
            break
        else:
            screen.clear()
            print("Selecione uma opção valida...")
            sleep(2)

if linhas[posicao_tipo] == "aluno":
    print("Aluno entrou")

if linhas[posicao_tipo] == "motorista":
    print("motorista entrou")
    
