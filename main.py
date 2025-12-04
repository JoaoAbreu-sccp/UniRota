from functions import GeralDef, screen
from time import sleep
from datetime import datetime
import csv
import os
import sys


screen.clear()
csv_gerado = False


while True:
    tipo_de_usuario=None
    logins = open("logins.txt")
    linhas = logins.read().splitlines()
    logins.close()

    screen.menu()
    while True:
        try:
            opc = int(input("\nEscolha uma opção(1-3): "))
            if 0 <= opc <= 6:
                break
            else:
                print("\nPor favor, insira uma opção valida!")
                input("\nPressione ENTER para voltar...") 

        except ValueError:
            print("Por favor digite um número inteiro!")
    screen.clear()
        
    if opc == 1:
        email = input("Digite o Email de Login: ").strip()
        senha = input("Digite a senha de acesso: ").strip()
        if email in linhas:
            posicao_senha = linhas.index(email) + 1
            if linhas[posicao_senha] == senha:
                posicao_tipo = linhas.index(email) - 1
                tipo_de_usuario = linhas[posicao_tipo]
            else:
                print("Email ou senha incorretos...")
                sleep(2)
                screen.clear()
        else:
            print("Email ou senha incorretos...")
            sleep(2)
            screen.clear()
    elif opc == 2:
        email = input("Digite o email cadastrado: ")
        if email.endswith("@gmail.com"):
            GeralDef.PasswordReset(email)
        else:
            print("Insira um email válido")
        sleep(2)
        screen.clear()
    elif opc == 3:
        print("Saindo do sistema... Até logo!")
        sys.exit()
        
    
    else:
        print("Selecione uma opção válida!")
        input("\nPressione ENTER para voltar...")
        screen.clear()
        
    
    if tipo_de_usuario is not None:

        if tipo_de_usuario == "administrador":
            while True:
                tipo_de_usuario == ""
                screen.clear()
                screen.menuADM()
                opc = int(input("opc = "))
                if opc == 1:
                    screen.clear()
                    listaalunos = open("listaalunos.txt")
                    linhasalunos = listaalunos.read().splitlines()
                    listaalunos.close()
                    print("Lista de Alunos:")
                    print(
                        f"{'#':3}{'Nome':21}{'Instituição':21}  {'P. Embarque':21}  {'P. Desembarque':21}  {'Conf. Ida':21}  {'Conf. Volta':21}"
                    )
                    index = 0
                    for c, info in enumerate(linhasalunos):
                        if c % 7 == 0 or c == 0:
                            if info != "":
                                index += 1
                                print(f"{index}. {info:18}", end=" | ")
                            else:
                                print()
                        else:
                            if info != "":
                                print(f"{info:20}", end=" | ")
                            else:
                                print()
                        csv_gerado = False
                    while True:
                        if not csv_gerado:
                            opc_1 = int(
                                input("""\n[1]: Exportar para CSV\n[0]: Sair\n\nDigite: """)
                            )
                        else:
                            opc_1 = int(input("\n[0]: Sair\n\nDigite: "))
                        if opc_1 == 1:
                            screen.clear()
                            print("Exportando...")
                            sleep(0.2)
                            with open(
                                "alunos_exportados.csv", "w", newline="", encoding="cp1252"
                            ) as csvfile:
                                writer = csv.writer(csvfile)
                                writer.writerow(
                                    [
                                        "Nome",
                                        "Instituição",
                                        "P. Embarque",
                                        "P. Desembarque",
                                        "Conf. Ida",
                                        "Conf. Volta",
                                    ]
                                )
                                for i in range(0, len(linhasalunos), 7):
                                    bloco = linhasalunos[i : i + 7]
                                    if len(bloco) >= 6:
                                        writer.writerow(bloco[:6])
                                print("Exportado com sucesso para 'alunos_exportados.csv'!")
                                csv_gerado = True
                                sleep(1)
                        elif opc_1 == 0:
                            print("Saindo...")
                            sleep(0.5)
                            break
                        else:
                            print("Opção inválida! Tente novamente.")
                    sleep(0.5)
                    screen.clear()
                elif opc == 2:
                    screen.clear()
                    print("Editar Universidades")
                elif opc == 3:
                    screen.clear()
                    opc_1 = screen.editar_usuário_menu("aluno")
                    if opc_1 == 1:
                        screen.clear()
                        GeralDef.Adicionar_usuario("aluno")
                    elif opc_1 == 2:
                        GeralDef.Excluir_usuario("aluno")
                    elif opc_1 == 3:
                        GeralDef.Editar_usuário("aluno")
                elif opc == 4:
                    screen.clear()
                    opc_1 = screen.editar_usuário_menu("motorista")
                    if opc_1 == 1:
                        GeralDef.Adicionar_usuario("motorista")
                    elif opc_1 == 2:
                        GeralDef.Excluir_usuario("motorista")
                    elif opc_1 == 3:
                        GeralDef.Editar_usuário("motorista")
                elif opc == 5:
                    screen.clear()
                    print("Acompanhar Rota")
                elif opc == 6:
                    while True:
                        screen.clear()
                        print(
                            """
            -------------------------
                 Adicionar Aviso 
            -------------------------

            [1]: Criar Aviso
            [2]: Visualizar Avisos
            [3]: Voltar"""
                            )
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
                elif opc == 7:
                    while True:
                        screen.clear()
                        opc_1 = screen.menuADM_sua_conta()
                        if opc_1 == 1:
                            GeralDef.Sua_conta(tipo_de_usuario)
                        elif opc_1 == 2:
                            GeralDef.Credenciais(tipo_de_usuario)
                        elif opc_1 == 0:
                            break
                        else:
                            print("Por favor insira uma opção valida! ")
                    break
                elif opc==0:
                    print("saindo...")
                    sleep(2)
                    break
                else:
                    screen.clear()
                    print("Selecione uma opção valida...")
                    sleep(2)

        elif linhas[posicao_tipo] == "aluno":
            screen.clear()
            pontoembarque = ["São sebastião", "Centro de Cultura", "Banco do Brasil", "Posto Pajet", "Garagem Brasileiro"]
            pontodesembarque = ["São sebastião", "Centro de Cultura", "Banco do Brasil", "Posto Pajet", "Garagem Brasileiro"]


            user_cache = {
                "Ponto de embarque": "",
                "Embarque na ida": "Não", 
                "Ponto de desembarque": "",
                "Embarque na volta": "Não",
                "Horário": "", 
            }



            dados_aluno = {
                "Nome": "Eduardo Moreira Santos Barreto",
                "Data de nascimento": "01/04/2005",
                "E-mail": "202511240025@ifba.edu.br",
                "Faculdade":"Institudo Federal de Educação Ciência e Tecnologia da Bahia (IFBA)",
                "CPF": "000.000.000-00",
                "RG": "0000000-00",
                "Telefone": "+55 (73) 9 4002-8922"
            }



            def cabecalho(texto="página inicial"):
                print(f"------------------------------{texto}------------------------------")
                print()

            def paginainicial():
                print('''
Bem vindo ao painel do aluno

[1]: Confirmar Check-in
[2]: Cancelar Check-in          
[3]: Dados pessoais
[4]: Acompanhar rota
[5]: Visualizar Avisos          
[6]: Sair      
                      ''')

            def confirmarpartida():
                screen.clear()
                cabecalho("CONFIRMAR PARTIDA")


                print("\nDefina o ponto de EMBARQUE (IDA): ")
                for i, pontos in enumerate(pontoembarque):
                    print(f"\n[{i+1}] - {pontos}") 

                escolha_ida = 0

                while not (1 <= escolha_ida <= len(pontoembarque)):
                    try:
                        escolha_ida = int(input(f'\nEscolha o ponto de embarque (1-{len(pontoembarque)}): '))
                        if not (1 <= escolha_ida <= len(pontoembarque)):
                            print("Opção inválida. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Digite um número.")


                user_cache["Ponto de embarque"] = pontoembarque[escolha_ida - 1] 

                ida = input(f"\nDeseja confirmar o embarque na IDA no ponto {user_cache["Ponto de embarque"]}? [s/n]: ").lower()
                if ida.startswith('s'):
                    user_cache["Embarque na ida"] = "Sim"
                else:
                    user_cache["Embarque na ida"] = "Não"

                screen.clear()
                cabecalho("CONFIRMAR PARTIDA")


                print("\nDefina o ponto de DESEMBARQUE (VOLTA): ")
                for i, pontos in enumerate(pontodesembarque):
                    print(f"\n[{i+1}] - {pontos}")

                escolha_volta = 0

                while not (1 <= escolha_volta <= len(pontodesembarque)):
                    try:
                        escolha_volta = int(input(f'\nEscolha o ponto de desembarque (1-{len(pontodesembarque)}): '))
                        if not (1 <= escolha_volta <= len(pontodesembarque)):
                            print("Opção inválida. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Digite um número.")


                user_cache["Ponto de desembarque"] = pontodesembarque[escolha_volta - 1]

                volta = input(f"Deseja confirmar o embarque na VOLTA no ponto {user_cache["Ponto de desembarque"]}? [s/n]: ").lower()
                if volta.startswith('s'):
                    user_cache["Embarque na volta"] = "Sim"
                else:
                    user_cache["Embarque na volta"] = "Não"
                screen.clear()



                if user_cache["Embarque na ida"] == "Não" and user_cache["Embarque na volta"] == "Não":
                    cabecalho("CHECK-IN CANCELADO")
                    print("Você não confirmou a ida nem a volta.")
                    print("Nenhum registro foi salvo.")

                else:

                    checkin = datetime.now()
                    checkin_formatado = checkin.strftime("%d/%m/%Y às %H:%M")


                    print(f"---INFORMAÇÕES GERAIS DO EMBARQUE---\n")

                    print(f"Check-in realizado no dia {checkin_formatado}")

                    if user_cache["Embarque na ida"] == "Sim":
                        print(f"IDA: CONFIRMADA✅")
                        print(f"Ponto de embarque: {user_cache['Ponto de embarque']}\n")
                        user_cache["Horário"] = checkin_formatado
                    else:
                        print(f"STATUS IDA: CANCELADA❌\n")


                    if user_cache["Embarque na volta"] == "Sim":
                        print(f"VOLTA: CONFIRMADA✅")
                        print(f"Ponto de desembarque: {user_cache['Ponto de desembarque']}\n")
                        user_cache["Horário"] = checkin_formatado
                    else:
                        print(f"STATUS VOLTA: CANCELADA❌\n")


                input("\nPressione ENTER para voltar à página inicial...")
                screen.clear()


            def dadospessoais():
                screen.clear()
                cabecalho("DADOS PESSOAIS")
                for chave, valor in dados_aluno.items():
                    print(f" {chave}: {valor}")
                print()
                input("\nPressione ENTER para voltar à página inicial...")
                screen.clear()

            def avisos():
                pasta_do_aviso = os.path.dirname(os.path.abspath(__file__))
                caminho_arquivo = os.path.join(pasta_do_aviso, "avisos.txt")
                avisos = open(caminho_arquivo, "r", encoding="utf-8")
                linhasavisos = avisos.read().splitlines()
                avisos.close()         
                for aviso in linhasavisos:
                    print(aviso)
                voltar = input("\nPressione ENTER para voltar...") 
                screen.clear()

            def cancelarcheckin():
                if user_cache["Horário"] != "" and user_cache["Embarque na ida"] == "Sim" and user_cache["Embarque na volta"] == "Sim":
                    print(f"Olá, você tem um check-in IDA e VOLTA confirmados no dia {user_cache['Horário']}.")

                    print("\nDeseja realizar alguma alteração?")

                    print("\n[1] Cancelar apenas a IDA")
                    print("[2] Cancelar apenas a VOLTA")
                    print("[3] Cancelar AMBOS (Ida e Volta")
                    print("[4] Não cancelar nada")


                    escolha_cancelar = str(input("\nEscolha uma opção(1-4): "))

                    if escolha_cancelar == "1":
                        screen.clear()
                        user_cache["Embarque na ida"] = "Não"
                        print("\nA IDA foi cancelada, a VOLTA permanece agendada.")
                        input("\nPressione ENTER para voltar...") 
                    elif escolha_cancelar == "2":
                        screen.clear()
                        user_cache["Embarque na volta"] = "Não"
                        print("\nA VOLTA foi cancelada, a IDA permanace agendada.")
                        input("\nPressione ENTER para voltar...") 
                    elif escolha_cancelar == "3":
                        screen.clear()
                        user_cache["Embarque na ida"] = "Não" 
                        user_cache["Embarque na volta"] = "Não"
                        user_cache["Horário"] = ""
                        print("\nIDA e VOLTA foram cancelados")
                        input("\nPressione ENTER para voltar...") 
                    elif escolha_cancelar == "4":
                        screen.clear()
                        print("\nNenhuma alteração foi feita.")
                        input("\nPressione ENTER para voltar...") 
                        
                elif user_cache["Horário"] != "" and user_cache["Embarque na ida"] == "Sim":
                            print(f"Olá, você tem um check-in somente IDA confirmado no dia {user_cache['Horário']}.")
                            escolha = input("Deseja cancelar? [s/n]: ")
                            if escolha == "s":
                                user_cache["Horário"] = ""
                                print("Seu check-in foi cancelado com sucesso!")
                                input("\nPressione ENTER para voltar...") 
                                screen.clear()
                            elif escolha == "n":
                                print("Certo! Voltando para o menu principal...")
                                input("\nPressione ENTER para voltar...") 
                                screen.clear()

                elif user_cache["Horário"] != "" and user_cache["Embarque na volta"] == "Sim":
                    print(f"Olá, você tem um check-in somente VOLTA confirmado no dia {user_cache['Horário']}.")
                    escolha = input("Deseja cancelar? [s/n]: ")
                    if escolha == "s":
                     user_cache["Horário"] = ""
                     print("Seu check-in foi cancelado com sucesso!")
                     input("\nPressione ENTER para voltar...") 
                     screen.clear()
                    elif escolha == "n":
                     print("Certo! Voltando para o menu principal...")
                     input("\nPressione ENTER para voltar...") 
                     screen.clear()
                    else:
                        print("\nOpção inválida.")

                else:
                    print("Você não tem nenhum check-in confirmado para cancelar.")
                    input("\nPressione ENTER para voltar...")  
                    screen.clear()

            def acompanharota():
                pasta_da_rota = os.path.dirname(os.path.abspath(__file__))
                caminho_rota = os.path.join(pasta_da_rota, "rota.txt")
                rota = open(caminho_rota, "r", encoding="utf-8")
                linhasrotas = rota.read().splitlines()
                rota.close()
                for rota in linhasrotas:
                    print(rota)
                voltar = str(input("\nDigite ENTER para voltar..."))
                screen.clear()

            while True: 
                paginainicial()
                try:

                    opcao01 = int(input("Insira a opção que deseja: "))

                    if opcao01 == 1:
                        screen.clear()
                        confirmarpartida()

                    elif opcao01 == 2:
                        screen.clear()
                        cabecalho("CANCELAR CHECK-IN")
                        cancelarcheckin()


                    elif opcao01 == 3:
                        screen.clear()
                        dadospessoais()
                        cabecalho("DADOS PESSOAIS")

                    elif opcao01 == 4:
                        screen.clear()
                        cabecalho("ACOMPANHAR ROTA")
                        acompanharota()
                        sleep(2)
                        screen.clear()

                    elif opcao01 == 5:
                        screen.clear()
                        cabecalho("AVISOS")
                        avisos()

                    elif opcao01 == 6:
                        print("Saindo do sistema... Até logo.")
                        sleep(1)
                        screen.clear()
                        break 
                    
                    else:
                        print("Opção inválida. Tente novamente.")
                        sleep(1)
                        screen.clear()

                except ValueError:
                    print("Entrada inválida. Por favor, digite um número (1-4).")
                    sleep(1)
                    screen.clear()

        elif linhas[posicao_tipo] == "motorista":

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
                    print(f"{'#':<3} | {'Check':<11} | {'Ponto de Parada':<25} | {'Endereço':<50}")
                    print("-" * 105)
                    for i in range(0, len(arq), 3):
                        ponto = arq[i + 1].strip()
                        end = arq[i + 2]

                        if i + 2 < len(arq):
                            check = arq[i].strip()
                        else:
                            check = ""
                        if check == "":
                            print(f"{i // 3 + 1:<3} | {'/':<11} | {ponto:<25} | {end:<50}")
                            newcheck = input("Check [True|False]: ").strip()
                            print()
                            arq[i] = newcheck
                            with open("rota.txt", "w") as rota:
                                rota.write("\n".join(arq))
                        else:
                            print()
                            print(f"{i // 3 + 1:<3} | {check:<11} | {ponto:<25} | {end:<50}")
                            if check == "False":
                                mod = input("Deseja modificar o check [s/n]: ")

                                if mod == "s":
                                    newcheck = input("Novo Check [True|False]: ").strip()
                                    arq[i] = newcheck

                    with open("rota.txt", "w") as rota:
                        rota.write("\n".join(arq))
                    print("\nRota atualizada com sucesso")
                    opc = int(input("\nDigite [1] para voltar:  "))
                    sleep(0.5)
                    screen.clear()
                elif opc == 3:
                    while True:
                        screen.clear()
                        print('''
[1]: Criar Aviso
[2]: Visualizar Avisos
[3]: Voltar
''')
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
        else:
            print("")
