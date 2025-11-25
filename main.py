from functions import GeralDef, screen
from datetime import datetime
from time import sleep
import os

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
if linhas[posicao_tipo] == "administrador":
    print("Adm entrou")

if linhas[posicao_tipo] == "aluno":
    print("Aluno entrou")

if linhas[posicao_tipo] == "motorista":
    print("motorista entrou")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



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
    "Nome": "Pedro Henrique Souza Oliveira",
    "Data de nascimento": "16/01/2005",
    "E-mail": "Pesouza544@gmail.com",
    "Faculdade": "Ifba",
    "CPF": "945.325.321.-29",
    "RG": "1212563-23",
    "Telefone": "+55 73 9 98612778"
}



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

def confirmarpartida():
    clear()
    cabecalho("CONFIRMAR PARTIDA")
    
   
    print("\nDefina o ponto de EMBARQUE (IDA): ")
    for i, pontos in enumerate(pontoembarque):
        print(f"[{i+1}] - {pontos}") 
    
    escolha_ida = 0
    
    while not (1 <= escolha_ida <= len(pontoembarque)):
        try:
            escolha_ida = int(input(f'\nEscolha o ponto de embarque (1-{len(pontoembarque)}): '))
            if not (1 <= escolha_ida <= len(pontoembarque)):
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    
    
    user_cache["Ponto de embarque"] = pontoembarque[escolha_ida - 1] # -1 para ajustar o índice
    
    ida = input(f"Deseja confirmar o embarque na IDA no ponto {user_cache["Ponto de embarque"]}? [s/n]: ").lower()
    if ida.startswith('s'):
        user_cache["Embarque na ida"] = "Sim"
    else:
        user_cache["Embarque na ida"] = "Não"

    clear()
    cabecalho("CONFIRMAR PARTIDA")

    
    print("\nDefina o ponto de DESEMBARQUE (VOLTA): ")
    for i, pontos in enumerate(pontodesembarque):
        print(f"[{i+1}] - {pontos}")

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

    clear()

  

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
    clear()


def dadospessoais():
    clear()
    cabecalho("DADOS PESSOAIS")
    for chave, valor in dados_aluno.items():
        print(f" {chave}: {valor}")
    print()
    input("\nPressione ENTER para voltar à página inicial...")
    clear()

def avisos():
    pasta_do_aviso = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(pasta_do_aviso, "avisos.txt")
    avisos = open(caminho_arquivo, "r", encoding="utf-8")
    linhasavisos = avisos.read().splitlines()
    avisos.close()         
    for aviso in linhasavisos:
        print(aviso)
    voltar = str(input("\nDigite [1] para voltar: "))
    clear()

def cancelarcheckin():
    if user_cache["Horário"] != "":
                print(f"Olá, você tem um check-in confirmado no dia {user_cache['Horário']}.")
                escolha = input("Deseja cancelar? [s/n]: ")
                if escolha == "s":
                    user_cache["Horário"] = ""
                    print("Seu check-in foi cancelado com sucesso!")
                    sleep(1.5)
                    clear()
                elif escolha == "n":
                    print("Certo! Voltando para o menu principal...")
                    sleep(2)
                    clear()


                   
    else:
        print("Você não tem nenhum check-in confirmado para cancelar.")
        input("\nPressione ENTER para voltar...")  
        clear()

while True: 
    paginainicial()
    try:
        
        opcao01 = int(input("Insira a opção que deseja: "))
        
        if opcao01 == 1:
            clear()
            confirmarpartida()
        
        elif opcao01 == 2:
            clear()
            cabecalho("CANCELAR CHECK-IN")
            cancelarcheckin()
            
        
        elif opcao01 == 3:
            clear()
            dadospessoais()
            cabecalho("DADOS PESSOAIS")
        
        elif opcao01 == 4:
            clear()
            cabecalho("ACOMPANHAR ROTA")
            print("calma pai")
            sleep(2)
            clear()

        elif opcao01 == 5:
            clear()
            cabecalho("AVISOS")
            avisos()
            
        elif opcao01 == 6:
            print("Saindo do sistema... Até logo.")
            sleep(1)
            clear()
            break 
        
        else:
            print("Opção inválida. Tente novamente.")
            sleep(1)
            clear()

    except ValueError:
        print("Entrada inválida. Por favor, digite um número (1-4).")
        sleep(1)
        clear()
   
   
   
   








     
    












