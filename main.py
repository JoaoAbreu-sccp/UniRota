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
            opc = int(input("\nEscolha uma opção: "))
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
                nome_usuario=linhas.index(email) - 2
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
    elif opc == 0:
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
                    while True:
                        screen.clear()
                        screen.menuUniversidades()
                        subopc = input("Opção: ")
                        if subopc == "1":
                            GeralDef.cadastrar_universidade()
                        elif subopc == "2":
                            GeralDef.listar_universidades()
                        elif subopc == "3":
                            GeralDef.editar_universidade()
                        elif subopc == "4":
                            GeralDef.excluir_universidade()
                        elif subopc == "0":
                            break
                        else:
                            print("Opção inválida!")
                            sleep(1)
                            
                elif opc == 3:
                    while True:
                        screen.clear()
                        opc_1 = screen.editar_usuário_menu("aluno")
                        if opc_1==1:
                            screen.clear()
                            GeralDef.visualizar_usuários("alunos")
                            sair=input("\n[ENTER] para voltar: ")
                        elif opc_1 == 2:
                            screen.clear()
                            GeralDef.Adicionar_usuario("aluno")
                        elif opc_1 == 3:
                            screen.clear()
                            GeralDef.Excluir_usuario("aluno")
                        elif opc_1 == 4:
                            screen.clear()
                            GeralDef.Editar_usuário("aluno")
                        elif opc_1==0:
                            break

                elif opc == 4:
                    while True:
                        screen.clear()
                        opc_1 = screen.editar_usuário_menu("motorista")
                        if opc_1 == 1:
                            screen.clear()
                            GeralDef.visualizar_usuários("motoristas")
                            sair=input("\n[ENTER] para voltar: ")
                        elif opc_1 == 2:
                            screen.clear()
                            GeralDef.Adicionar_usuario("motorista")
                        elif opc_1 == 3:
                            screen.clear()
                            GeralDef.Excluir_usuario("motorista")
                        elif opc_1 == 4:
                            screen.clear()
                            GeralDef.Editar_usuário("motorista")
                        elif opc_1 == 0:
                            break
                            
                            
                elif opc == 5:
                    screen.clear()
                    opc=screen.rota()
                    if opc==1:
                        GeralDef.mostrar_rota()
                        passar=input("Pressione [ENTER] para voltar\n")
                    elif opc==2:
                        GeralDef.adicionar_ponto()
                        print ("Rota alterado com sucesso")
                        sleep(0.5)
                        print("Imprimindo nova rota")
                        sleep(0.7)
                        screen.clear()
                        sleep(0.3)
                        GeralDef.mostrar_rota()
                    elif opc==3:
                        GeralDef.remover_ponto()
                        print ("Rota alterado com sucesso")
                        sleep(0.5)
                        print("Imprimindo nova rota")
                        sleep(0.7)
                        screen.clear()
                        sleep(0.3)
                        GeralDef.mostrar_rota()
                    
                elif opc == 6:
                    while True:
                        screen.clear()
                        screen.menuAVISO()
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
                            voltar = str(input("\nDigite [0] para voltar: "))
                        elif opc == 3:
                            avisos = open("avisos.txt", "r", encoding="utf-8")
                            linhasavisos = avisos.read().splitlines()
                            avisos.close()
                            screen.clear()
                            indice = 0
                            for aviso in linhasavisos:
                                indice += 1
                                print(f"[{indice}] {aviso}")
                                
                            print()
                            print("[1] Para Editar Aviso")
                            print("[2] Para Excluir Aviso")
                            print("[0] Para voltar")
                            opcaviso = int(input("opc = "))
                            if opcaviso == 1:
                                index = int(input("Digite o número do aviso que deseja EDITAR [0 para cancelar]: "))
                                if index == 0:
                                    continue
                                elif index > indice or index < 1:
                                    print("Opção invalida...")
                                    sleep(0.5)
                                    continue
                                print("Digite a nova versão do aviso:")
                                texto = str(input("-> "))
                                GeralDef.EditarAviso(index-1, texto)
                                print("Aviso editado com successo!")
                                sleep(0.5)
                            elif opcaviso == 2:
                                index = int(input("Digite o número do aviso que deseja EXCLUIR [0 para cancelar]: "))
                                if index == 0:
                                    continue
                                elif index > indice or index < 1:
                                    print("Opção invalida...")
                                    sleep(0.5)
                                    continue
                                GeralDef.ExcluirAviso(index-1)
                                print("Aviso Excluido com sucesso!")
                                sleep(0.5)

                                
                        elif opc == 0:
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
                    screen.clear()
                    break
                else:
                    screen.clear()
                    print("Selecione uma opção valida...")
                    sleep(2)




#início do bloco de códigos do aluno----------------------------------------------------------
        elif linhas[posicao_tipo] == "aluno":
            screen.clear()
            

            def cabecalho(texto="página inicial"):
                print(f"------------------------------{texto}------------------------------")
                print()


            

            while True: 
                GeralDef.paginainicial()
                try:

                    opcao01 = int(input("Insira a opção que deseja: "))

                    if opcao01 == 1:
                        screen.clear()
                        GeralDef.confirmarpartida()

                    elif opcao01 == 2:
                        screen.clear()
                        cabecalho("CANCELAR CHECK-IN")
                        GeralDef.cancelarcheckin()


                    elif opcao01 == 3:
                        screen.clear()
                        GeralDef.dadospessoais()
                        cabecalho("DADOS PESSOAIS")

                    elif opcao01 == 4:
                        screen.clear()
                        cabecalho("ACOMPANHAR ROTA")
                        GeralDef.acompanharota()
                        sleep(2)
                        screen.clear()

                    elif opcao01 == 5:
                        screen.clear()
                        cabecalho("AVISOS")
                        GeralDef.avisos()

                    elif opcao01 == 0:
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
#final do bloco de código do aluno------------------------------------------------------------




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
                    with open("rota.txt","r", encoding="utf-8") as arquivo:
                        arq = arquivo.read().splitlines()

                    while True:
                        print(f"{'#':<3} | {'Check':<11} | {'Ponto de Parada':<30} | {'Endereço':<40}")
                        print("-" * 130)
                        
                        for i in range(0, len(arq), 3):
                            ponto = arq[i + 1].strip()
                            end = arq[i + 2]
                            check = arq[i].strip()
                        
                            print(f"{i // 3 + 1:<3} | {check:<11} | {ponto:<30} | {end:<40}")
                            print("-" * 130)

                        print()
                        
                        print("[1]: Dar Check ✅\n[2]: Remover Check ❌\n[3]: Sair 🚪")
                        print("=" * 50)
                        try:
                            opcao = int(input("Escolha uma opção (1-3): "))
                        except ValueError:
                            print("Entrada inválida. Digite um número inteiro")
                            sleep(0.5)
                            screen.clear()
                        else:
                            if opcao == 1:
                                print("=" * 50)
                                try:
                                    check_novo = int(input("Digite o número do ponto para dar check: "))
                                except ValueError:
                                    print("Digite um número inteiro válido.")
                                else:
                                    print("=" * 50)
                                    comfirm = input("Tem certeza? [s/n] ")
                                    if comfirm == "s":
                                        arq[(check_novo - 1) * 3] = "✅"
                                        print("\nRota atualizada com sucesso")
                                    
                            
                            elif opcao == 2:
                                print("=" * 50)
                                try:
                                    check_novo = int(input("Digite o número do ponto para remover o check: "))
                                    print("=" * 50)
                                except ValueError:
                                    print("Entrada inválida. Digite um número inteiro")
                                else:
                                    comfirm = input("Tem certeza? [s/n] ")
                                    if comfirm == "s":
                                        arq[(check_novo - 1) * 3] = "❌"
                                        print("\nRota atualizada com sucesso")
                                        

                            elif opcao == 3:
                                sleep(0.5)
                                screen.clear()
                                break
                            
                            else:
                                print("Opção inválida! Tente novamente.")

                            with open("rota.txt", "w", encoding="utf-8") as rota:
                                rota.write("\n".join(arq))
                        
                            voltar = str(input("\nDigite [1] para voltar: "))
                            sleep(0.5)
                            screen.clear()

                elif opc == 3:
                    while True:
                        screen.clear()
                        screen.menuAVISO()
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
                            voltar = str(input("\nDigite [0] para voltar: "))
                        elif opc == 0:
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
