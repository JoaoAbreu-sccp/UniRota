from time import sleep
from functions import screen
import json
import os


def PasswordReset(email):
    from random import randint

    logins = open("logins.txt")
    linhas = logins.read().splitlines()
    logins.close()

    if email in linhas:
        codigo_reset = f"{randint(0, 999999):06}"

        reset = open("codigo.txt", "w")
        reset.write(codigo_reset + "\n")
        reset.close()

        reset = open("codigo.txt", "r")
        codigoreset = reset.read().splitlines()
        reset.close()

        print("Se esse email estiver cadastrado, ensira o código que foi enviado")
        codigo = input("Digite o código de reset: ")

        if codigo == codigoreset[0]:
            posicao_senha = linhas.index(email) + 1
            linhas[posicao_senha] = input("Digite a nova senha: ")
            logins = open("logins.txt", "w")
            logins.writelines([linha + "\n" for linha in linhas])
            logins.close()
            print("Senha alterada com sucesso!")
        else:
            print("Código incorreto!")
    else:
        print("Se esse email estiver cadastrado, ensira o código que foi enviado")
        codigo = input("Digite o código de reset: ")
        print("Código incorreto!")

def gerar_lista_confirmacao_json():
    with open("logins.txt", "r", encoding="utf-8") as f:
        linhas = [l for l in f.read().splitlines() if l.strip()]

    alunos = []

    for i, linha in enumerate(linhas):
        if linha == "aluno":
            bloco = linhas[i:i+9]
            alunos.append({
                "Nome": bloco[3],
                "Instituição": bloco[4]
            })

    try:
        with open("banco_alunos.json", "r", encoding="utf-8") as f:
            lista_antiga = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_antiga = []

    mapa_antigo = {a["Nome"]: a for a in lista_antiga}

    nova_lista = []

    for aluno in alunos:
        nome = aluno["Nome"]
        instituicao = aluno["Instituição"]

        if nome in mapa_antigo:
            item = mapa_antigo[nome]
            item["Instituição"] = instituicao
            nova_lista.append(item)
        else:
            nova_lista.append({
                "Nome": nome,
                "Instituição": instituicao,
                "Ponto de embarque": "-",
                "Ponto de desembarque": "-",
                "Embarque na ida": "Não",
                "Embarque na volta": "Não",
                "Horário": "-"
            })

    with open("banco_alunos.json", "w", encoding="utf-8") as f:
        json.dump(nova_lista, f, ensure_ascii=False, indent=4)



def printar_lista(ARQUIVO_BANCO):
    screen.clear()
    if not os.path.exists(ARQUIVO_BANCO):
        print("Nenhum banco de dados encontrado. Cadastre alguém primeiro!")
    else:
        with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
            banco_de_dados_alunos = json.load(arquivo)
            print("\n" + "="*110)
            print(f"{'LISTA DE ALUNOS':^110}")
            print("="*110)
            print(f"{'#':<3} {'Nome':<25} {'Instituição':<20} {'P. Embarque':<20} {'P. Desembarque':<20} {'Ida':<6} {'Volta':<6}")
            print("-" * 110)

        index = 0
        for info_aluno in banco_de_dados_alunos:
            n = info_aluno.get('Nome', '-')
            i = info_aluno.get('Instituição', '-')
            pe = info_aluno.get('Ponto de embarque', '-')
            pd = info_aluno.get('Ponto de desembarque', '-')
                                
            verif_ida = info_aluno.get('Embarque na ida', 'Não')
            if verif_ida == "Sim":
                status_ida = "✅"
            else:
                status_ida = "❌"
            verif_volta = info_aluno.get('Embarque na volta', 'Não')
            if verif_volta == "Sim":
                status_volta = "✅"
            else:
                status_volta = "❌"

            if verif_ida== "Sim" or verif_volta == "Sim":
                index+=1
                print(f"{index:<3} {n:<25} {i:<20} {pe:<20} {pd:<20} {status_ida:<6} {status_volta:<6}")
        print("-" * 110)

#admnistrador

def CreateNotice():
    from datetime import datetime

    while True:
        print("Digite o Aviso [SAIR para encerrar]:")
        text = str(input("-> "))
        if text.upper() == "SAIR":
            break
        date = datetime.now()
        date_time = date.strftime("%d/%m/%Y %H:%M:%S")
        novo_aviso = f"[{date_time}] {text}\n"

        arquivo = open("avisos.txt", "r", encoding="utf-8")
        conteudo_antigo = arquivo.read()
        arquivo.close()

        avisos = open("avisos.txt", "w", encoding="utf-8")
        avisos.write(novo_aviso + conteudo_antigo)
        avisos.close()

        print("Aviso salvo com sucesso")

def EditarAviso(index, texto, caminho="avisos.txt"):
    with open(caminho, "r", encoding="utf-8") as arq:
        avisos = arq.readlines()

    if 0 <= index < len(avisos):
        linha_original = avisos[index].rstrip("\n")
        prefixo = linha_original[:22]
        avisos[index] = f"{prefixo}[EDITADO] {texto}\n"

        with open(caminho, "w", encoding="utf-8") as arq:
            arq.writelines(avisos)

        return True

    return False

def ExcluirAviso(index, caminho="avisos.txt"):
    """Exclui o aviso no índice informado."""
    try:
        with open(caminho, "r", encoding="utf-8") as arq:
            avisos = arq.readlines()
    except FileNotFoundError:
        return False

    if 0 <= index < len(avisos):
        avisos.pop(index)

        with open(caminho, "w", encoding="utf-8") as arq:
            arq.writelines(avisos)

        return True 

    return False

def visualizar_usuários(tipo_de_usuario):
    with open("logins.txt", "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()
        alunos = []
        motoristas = []
        
    i = 0
    while i < len(linhas):

        if linhas[i] == "aluno":
            alunos.append(linhas[i+1 : i+10])
            i += 10

        elif linhas[i] == "motorista":
            motoristas.append(linhas[i+1 : i+9])
            i += 9
        
        else:
            i += 1
        
    if tipo_de_usuario == "alunos":
        for c, dados in enumerate(alunos):
            print(f"{c+1}: {dados[2]}")

    elif tipo_de_usuario == "motoristas":
        for c, dados in enumerate(motoristas):
            print(f"{c+1}: {dados[2]}")

def Editar_usuário(tipo_de_usuario_editado):
    alteracao_aluno = False
    alteracao_motoristas = False
    from time import sleep
    
    lista_a = [
            "nome",
            "Instituição",
            "Cpf",
            "Telefone",
            "Data de nascimento",
        ]
    
    lista_m = [
            "nome",
            "Cpf",
            "Telefone",
            "Data de nascimento",
        ]

    with open("logins.txt", "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()
        linhas_limpa = [linha for linha in linhas if linha != ""]
        alunos = []
        motoristas = []

        for c, linha in enumerate(linhas_limpa):
            if linha == "aluno":
                alunos.append(linhas_limpa[c : c + 9])
            if linha == "motorista":
                motoristas.append(linhas_limpa[c : c + 8])

    if tipo_de_usuario_editado == "aluno":
        if not alunos:
            print("Não há nenhum aluno cadastrados!")
        else:
            print("\nAlunos cadastrados:")
        for i, aluno in enumerate(alunos):
            nome = aluno[3]
            print(f"[{i+1}] - {nome}")

        indice = input("\nDigite o número do aluno que deseja editar Digite [Sair] para cancelar: ")
        if indice.lower()=="sair":
            return 0
        if indice.isdigit():
            aluno = alunos[int(indice)-1]

            cpf_formatado = f"{aluno[5][:3]}.{aluno[5][3:6]}.{aluno[5][6:9]}-{aluno[5][9:]}"
            telefone_formatado = f"({aluno[6][:2]}){aluno[6][2:7]}-{aluno[6][7:]}"
            data_formatada = f"{aluno[7][:2]}/{aluno[7][2:4]}/{aluno[7][4:]}"

            print("\nInformações atuais:")
            print(
            f"""1 - Nome: {aluno[3]}
2 - Instituição: {aluno[4]}
3 - Cpf: {cpf_formatado}
4 - Telefone: {telefone_formatado}
5 - Data de nascimento {data_formatada}"""
        )

            campo = 0
        
            while True:
                campo = input("\nQual campo deseja editar (1-5)? Digite [Sair] para cancelar: ")
                if campo.lower() == "sair":
                    break

                if campo.isdigit():
                    campo = int(campo)
                    if 1 <= campo <= 5:
                        novo_valor = input(f"Digite o novo valor para {lista_a[campo-1]}: ")
                        aluno[campo + 2] = novo_valor
                        alunos[int(indice)-1] = aluno
                        alteracao_aluno = True
                        break
                    else:
                        print("Por favor insira um número entre 1 e 5!")
                else:
                    print("Entrada inválida! Digite um número ou 'sair'.")


    if tipo_de_usuario_editado == "motorista":
        if not motoristas:
            print("Não há nenhum motorista cadastrados!")
        else:
            print("\nMotoristas cadastrados:")
        for i, motorista in enumerate(motoristas):
            nome = motorista[3]
            print(f"[{i+1}] - {nome}")

        indice = (input("\nDigite o número do motorista que deseja editar: [Sair] para cancelar: "))
        if indice.lower()=="sair":
            return 0
        
        if indice.isdigit():
            motorista = motoristas[int(indice)-1]

            cpf_formatado = f"{motorista[4][:3]}.{motorista[4][3:6]}.{motorista[4][6:9]}-{motorista[4][9:]}"
            telefone_formatado = (f"({motorista[5][:2]}){motorista[5][2:7]}-{motorista[5][7:]}")
            data_formatada = f"{motorista[6][:2]}/{motorista[6][2:4]}/{motorista[6][4:]}"

            print("\nInformações atuais:")
            print(
                f"""1 - Nome: {motorista[3]}
2 - Cpf: {cpf_formatado}
3 - Telefone: {telefone_formatado}
4 - Data de Nascimento {data_formatada}"""
            )

            while True:
                campo = (input("\nQual campo deseja editar (1-4)? [Sair] para cancelar: "))

                if campo.lower()=="sair":
                    break

                if 1 <= int(campo) <= 4:
                    novo_valor = input(f"Digite o novo valor para {lista_m[int(campo)-1]}: ")
                    motorista[int(campo) + 2] = novo_valor
                    motoristas[int(indice)-1] = motorista
                    alteracao_motoristas = True
                    break
                
                else:
                    print("Por favor insira um número entre 1 e 4!")

    if alteracao_aluno:
        inicio = linhas_limpa.index(aluno[0])
        linhas_limpa[inicio : inicio + len(aluno)] = aluno
        with open("logins.txt", "w", encoding="utf-8") as f:
            for i, linha in enumerate(linhas_limpa):
                f.write(linha + "\n")
                if linha == "-":
                    f.write("\n")
            print("\nInformação atualizada com sucesso!")
        sleep(3)

    if alteracao_motoristas:
        inicio = linhas_limpa.index(motorista[0])
        linhas_limpa[inicio : inicio + len(motorista)] = motorista
        with open("logins.txt", "w", encoding="utf-8") as f:
            for i, linha in enumerate(linhas_limpa):
                f.write(linha + "\n")
                if linha == "-":
                    f.write("\n")
        print("\nInformação atualizada com sucesso!")
        sleep(3)


def Adicionar_usuario(tipo_de_usuário_adicionado):

    adicao_aluno = False
    adicao_motorista = False

    with open("logins.txt", "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()
        linhas_limpa = [linha for linha in linhas if linha != ""]
        alunos = []
        motoristas = []

    lista = [
        "nome",
        "Instituição",
        "Cpf",
        "Telefone",
        "Data de nascimento",
    ]

    if tipo_de_usuário_adicionado == "aluno":
        for posição in linhas_limpa:
            posição == "motorista"
            indice = linhas_limpa.index(posição)

        novo_usuario = []
        novo_usuario.append("aluno")
        email = input("Digite o email do aluno: ")
        novo_usuario.append(email)
        novo_usuario.append("aluno123")
        nome = input("Digite o nome do aluno: ")
        novo_usuario.append(nome)
        Instituição = input("Digite a instituição do aluno: ")
        novo_usuario.append(Instituição)
        Cpf = input("Digite o cpf do aluno: ")
        novo_usuario.append(Cpf)
        Telefone = input("Digite o telefone do aluno: ")
        novo_usuario.append(Telefone)
        Data_de_nascimento = input("Digte a data de nascimento do aluno: ")
        novo_usuario.append(Data_de_nascimento)
        novo_usuario.append("-")

        while True:
            confirma_adicao=input("Confirmar adição [s/n]: ")
            if confirma_adicao=="s":
                adicao_aluno = True
                break
            elif confirma_adicao=="n":
                adicao_aluno = False
                break
            else:
                print("Por favor digite [s] ou [n]")


    elif tipo_de_usuário_adicionado == "motorista":

        novo_usuario = []
        novo_usuario.append("motorista")
        email = input("Digite o email do motorista: ")
        novo_usuario.append(email)
        novo_usuario.append("moto123")
        nome = input("Digite o nome do motorista: ")
        novo_usuario.append(nome)
        Cpf = input("Digite o cpf do motorista: ")
        novo_usuario.append(Cpf)
        Telefone = input("Digite o cpf do motorista: ")
        novo_usuario.append(Cpf)
        Data_de_nascimento=("Digite a da nascimento do motorista: ")
        novo_usuario.append(Data_de_nascimento)
        novo_usuario.append("-")
        
        while True:
            confirma_adicao=input("Confirmar adição [s/n]: ")
            if confirma_adicao.lower().strip()=="s":
                adicao_motorista = True
                break
            elif confirma_adicao.lower().strip()=="n":
                adicao_motorista = False
                break
            else:
                print("Por favor digite [s] ou [n]")


    linhas_limpa.extend(novo_usuario)

    if adicao_aluno:
        with open("logins.txt", "w", encoding="utf-8") as f:
            for i, linha in enumerate(linhas_limpa):
                f.write(linha + "\n")
                if linha == "-":
                    f.write("\n")

    if adicao_motorista:
        with open("logins.txt", "w", encoding="utf-8") as f:
            for i, linha in enumerate(linhas_limpa):
                f.write(linha + "\n")
                if linha == "-":
                    f.write("\n")



def Excluir_usuario(tipo_de_usuário_excluido):
    with open("logins.txt", "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()
        linhas_limpa = [linha for linha in linhas if linha != ""]
        alunos = []
        motoristas = []

        for c, linha in enumerate(linhas_limpa):
            if linha == "aluno":
                alunos.append(linhas_limpa[c : c + 9])
            if linha == "motorista":
                motoristas.append(linhas_limpa[c : c + 8])

    if tipo_de_usuário_excluido == "aluno":
        if not alunos:
            print("Não há nenhum aluno cadastrados!")
        else:
            print("\nAlunos cadastrados:")
        for i, aluno in enumerate(alunos):
            print(f"[{i+1}] - {aluno[3]}")   
        indice = int(input("\nDigite o número do aluno que deseja excluir: ")) - 1
        aluno_escolhido = alunos[indice]

        nome = aluno_escolhido[3]          
        pos_nome = linhas_limpa.index(nome)  

        inicio_bloco = pos_nome - 3         

        for _ in range(9):         
            linhas_limpa.pop(inicio_bloco)

    if tipo_de_usuário_excluido == "motorista":
        if not motoristas:
            print("Não há nenhum motorista cadastrados!")
        else:
            print("\nMotoristas cadastrados:")

        for i, motorista in enumerate(motoristas):
            print(f"[{i+1}] - {motorista[3]}")

        indice = int(input("\nDigite o número do motorista que deseja excluir: ")) - 1
        motorista_escolhido = motoristas[indice]

        nome = motorista_escolhido[3]
        pos_nome = linhas_limpa.index(nome)

        inicio_bloco = pos_nome - 3

        for _ in range(8):
            linhas_limpa.pop(inicio_bloco)
            

    with open("logins.txt", "w", encoding="utf-8") as f:
        for i, linha in enumerate(linhas_limpa):
            f.write(linha + "\n")
            if linha == "-":
                f.write("\n")

def Sua_conta(tipo_de_login):
    from random import randint

    with open("logins.txt", "r+", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines()]

        indície = linhas.index(tipo_de_login)
        print(f"""
    Login {tipo_de_login}

Nome: {linhas[indície+3]}
Data de Nascimento: {linhas[indície+6]}
Cpf: {linhas[indície+4]}
Telefone: {linhas[indície+5]}
              """)
        while True:
            opc = int(
                input(
                    """
[1] Alterar Telefone
[0] Voltar: 
                    
Digite: """))

            if opc == 1:
                print("O código de acesso foi enviado para seu número")
                codigo_reset = f"{randint(0, 999999):06}"

                with open("codigo.txt", "w", encoding="utf-8") as reset:
                    reset.write(codigo_reset + "\n")

                with open("codigo.txt", "r", encoding="utf-8") as reset:
                    codigoreset = reset.read().strip()

                codigo = input("Digte: ")
                if codigo == codigoreset:
                    linhas[indície + 5] = input("Digite seu novo telefone: ")

                    with open("logins.txt", "w", encoding="utf-8") as logins:
                        logins.writelines([linha + "\n" for linha in linhas])

                    print("Telefone alteraqdo com sucesso! ")
                else:
                    print("Codigo incorreto! ")
            elif opc == 0:
                break


def Credenciais(tipo_de_login):
    with open("logins.txt", "r+", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines()]

        indície = linhas.index(tipo_de_login)

        senha = linhas[indície + 2]
        while True:
            confirmar_senha = input(
                "Por favor insira sua senha para entrar neste campo: "
            )
            if confirmar_senha == senha:
                print(f"Senha atual: {senha}")
                opc = int(
                    input(
                        """
[1] Alterar senha
[0] Voltar

Digite: """
                    )
                )
                if opc == 1:
                    PasswordReset(linhas[indície + 1])
                if opc == 0:
                    break
            else:
                print("Senha incorreta! ")



def carregar_universidades():
    
    import os
    lista_universidades = []
    
    if not os.path.exists("lista_universidades.txt"):
        return lista_universidades

    with open("lista_universidades.txt", "r") as f:
        conteudo = f.read().strip()

    if not conteudo:
        return lista_universidades

    blocos = conteudo.split("---")

    for bloco in blocos:
        linhas = [x.strip() for x in bloco.splitlines() if x.strip()]
        if len(linhas) >= 3:
            lista_universidades.append({
                "nome": linhas[0],
                "cnpj": linhas[1],
                "endereco": linhas[2]})

    return lista_universidades

def salvar_universidades(lista_universidades):
    with open("lista_universidades.txt", "w") as f:
        for u in lista_universidades:
            f.write(f"{u['nome']}\n{u['cnpj']}\n{u['endereco']}\n---\n")

def cadastrar_universidade():
    nome = input("Nome: ").strip()
    cnpj = input("CNPJ: ").strip()
    endereco = input("Endereço: ").strip()

    if not nome or not cnpj or not endereco:
        print("Todos os campos são obrigatórios.")
        sleep(2)
        return

    lista_universidades = carregar_universidades()

    lista_universidades.append({
        "nome": nome,
        "cnpj": cnpj,
        "endereco": endereco})

    salvar_universidades(lista_universidades)

    print(f"\n:Universidade '{nome}' cadastrada com sucesso!")
    sleep(2)


def listar_universidades():
    screen.clear()
    lista_universidades = carregar_universidades()

    print('''\n---------------------------
 UNIVERSIDADES CADASTRADAS
---------------------------\n''')

    if not lista_universidades:
        print("Nenhuma universidade cadastrada.")
        input("\nPressione ENTER para continuar...")
        return
    for i, u in enumerate(lista_universidades, 1):
        print(f"[{i}] {u['nome']} | {u['cnpj']} | {u['endereco']}")

    input("\nPressione ENTER para continuar...")
def editar_universidade():
    lista_universidades = carregar_universidades()

    if not lista_universidades:
        print("Nenhuma universidade cadastrada.")
        sleep(2)
        return

    listar_universidades()

    entrada = input("\nDigite o número da universidade: ").strip()

    if not entrada.isdigit():
        print("Entrada inválida.")
        sleep(2)
        return

    i = int(entrada) - 1
    if not (0 <= i < len(lista_universidades)):
        print("Número inválido.")
        sleep(2)
        return

    u = lista_universidades[i]

    novo_nome = input(f"Novo nome ({u['nome']}): ").strip() or u['nome']
    novo_cnpj = input(f"Novo CNPJ ({u['cnpj']}): ").strip() or u['cnpj']
    novo_endereco = input(f"Novo Endereço ({u['endereco']}): ").strip() or u['endereco']

    lista_universidades[i] = {
        "nome": novo_nome,
        "cnpj": novo_cnpj,
        "endereco": novo_endereco}
    salvar_universidades(lista_universidades)

    print("Universidade atualizada com sucesso!")
    sleep(2)

def excluir_universidade():
    lista_universidades = carregar_universidades()
    if not lista_universidades:
        print("Nenhuma universidade cadastrada.")
        sleep(2)
        return

    listar_universidades()

    entrada = input("\nDigite o número para excluir: ").strip()
    if not entrada.isdigit():
        print("Entrada inválida.")
        sleep(2)
        return

    i = int(entrada) - 1

    if not (0 <= i < len(lista_universidades)):
        print("Número inválido.")
        sleep(2)
        return

    confirm = input(f"Excluir '{lista_universidades[i]['nome']}'? (s/n): ").lower()

    if confirm == "s":
        nome = lista_universidades[i]["nome"]
        del lista_universidades[i]
        salvar_universidades(lista_universidades)
        print(f"'{nome}' excluída com sucesso!")

    sleep(2)
    
def mostrar_rota():
    screen.clear()
    print("Rota\n")

    with open("rota.txt", "r", encoding="utf-8") as arquivo:
        arq = arquivo.read().splitlines()

    print(f"{'#':<3} | {'Check':<11} | {'Ponto de Parada':<25} | {'Endereço':<50}")
    print("-" * 105)

    for i in range(0, len(arq), 3):
        check = arq[i].strip()
        ponto = arq[i + 1].strip()
        end = arq[i + 2].strip()

        check_exibicao = check if check != "" else "/"

        print(f"{i // 3 + 1:<3} | {check_exibicao:<11} | {ponto:<25} | {end:<50}")

    print()
    input("Digite ENTER para voltar...")
    screen.clear()

def adicionar_ponto():
    screen.clear()
    print("Adicionar novo ponto à rota\n")

    check = "False"
    ponto = input("Nome do ponto de parada: ").strip()
    endereco = input("Endereço do ponto: ").strip()

    try:
        with open("rota.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        conteudo = ""

    with open("rota.txt", "a", encoding="utf-8") as arquivo:
        if len(conteudo) > 0 and not conteudo.endswith("\n"):
            arquivo.write("\n")

        arquivo.write(f"{check}\n{ponto}\n{endereco}\n")

    print("\nPonto adicionado com sucesso!")
    screen.clear()


def remover_ponto():
    screen.clear()
    print("Remover ponto da rota\n")

    with open("rota.txt", "r", encoding="utf-8") as arquivo:
        arq = arquivo.read().splitlines()

    print(f"{'#':<3} | {'Ponto de Parada':<25} | {'Endereço':<50}")
    print("-" * 90)

    pontos = []
    for i in range(0, len(arq), 3):
        check = arq[i]
        ponto = arq[i+1]
        end = arq[i+2]
        index = i // 3 + 1
        pontos.append((index, ponto, end))
        print(f"{index:<3} | {ponto:<25} | {end:<50}")

    try:
        escolha = int(input("\nNúmero do ponto para remover: "))
    except:
        print("Entrada inválida.")
        input("Voltar...")
        return

    if escolha <= 0 or escolha > len(pontos):
        print("Ponto inexistente.")
        input("Voltar...")
        return

    inicio = (escolha - 1) * 3
    fim = inicio + 3
    del arq[inicio:fim]

    with open("rota.txt", "w", encoding="utf-8") as arquivo:
        for linha in arq:
            arquivo.write(linha + "\n")

    print("\nPonto removido com sucesso!")
    screen.clear()


#alunos

def confirmarpartida(pontoembarque):
    screen.clear()
    screen.cabecalho("CONFIRMAR PARTIDA")
    

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
    
    ida = input(f"Deseja confirmar o embarque na IDA no ponto {user_cache['Ponto de embarque']}? [s/n]: ").lower()
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
    
    volta = input(f"Deseja confirmar o embarque na VOLTA no ponto {user_cache['Ponto de desembarque']}? [s/n]: ").lower()
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
[0]: Sair      
                      ''')

def confirmarpartida():
                
                
                from datetime import datetime

                pontoembarque = ["São sebastião", "Centro de Cultura", "Banco do Brasil", "Posto Pajet", "Garagem Brasileiro"]
                pontodesembarque = ["São sebastião", "Centro de Cultura", "Banco do Brasil", "Posto Pajet", "Garagem Brasileiro"]

                ARQUIVO_BANCO = "banco_alunos.json"

                user_cache = {
                "Nome": "",
                "Instituição": "",
                "Ponto de embarque": "",
                "Ponto de desembarque": "",
                "Embarque na ida": "Não", 
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






                screen.clear()
                cabecalho("CONFIRMAR PARTIDA")
                print('''
Deseja realizar o check-in?

[1]: Confirmar Check-in somente IDA
[2]: Confirmar Check-in somente VOLTA      
[3]: Confirmar Check-in IDA e VOLTA
[0]: Voltar                      
                      ''')

                escolha_checkin = str(input("\nEscolha uma opção: ")) 

                if escolha_checkin == "3":

                    nome = input("Digite seu nome: ")
                    
        
                    inst = input("Instituição: ")

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

                    ida = input(f"\nDeseja confirmar o embarque na IDA no ponto {user_cache['Ponto de embarque']}? [s/n]: ").lower()
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

                    volta = input(f"Deseja confirmar o embarque na VOLTA no ponto {user_cache['Ponto de desembarque']}? [s/n]: ").lower()
                    if volta.startswith('s'):
                        user_cache["Embarque na volta"] = "Sim"
                    else:
                        user_cache["Embarque na volta"] = "Não"
                    screen.clear()



                    if user_cache["Embarque na ida"] == "Não" and user_cache["Embarque na volta"] == "Não":
                        cabecalho("CHECK-IN CANCELADO")
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

                        novo_aluno = {
                        "Nome": nome,  
                        "Instituição": inst, 
                        "Ponto de embarque": user_cache["Ponto de embarque"], 
                        "Ponto de desembarque": user_cache["Ponto de desembarque"], 
                        "Embarque na ida": user_cache["Embarque na ida"],
                        "Embarque na volta": user_cache["Embarque na volta"],
                        "Horário": user_cache["Horário"]
                            }
                        
                        lista_atual = []
                        if os.path.exists(ARQUIVO_BANCO):
                            with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
                                try:
                                    lista_atual = json.load(arquivo) 
                                except:
                                    lista_atual = []

                        lista_atual.append(novo_aluno)
                        with open(ARQUIVO_BANCO, "w", encoding="utf-8") as arquivo:
                            json.dump(lista_atual, arquivo, indent=4, ensure_ascii=False)


                        input("\nPressione ENTER para voltar à página inicial...")
                        screen.clear()

                    





                elif escolha_checkin == "1":
                    screen.clear()
                    cabecalho("CONFIRMAR PARTIDA (SOMENTE IDA)")

                    nome = input("Digite seu nome: ")
                    inst = input("Instituição: ")

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

                    ida = input(f"\nDeseja confirmar o embarque na IDA no ponto {user_cache['Ponto de embarque']}? [s/n]: ").lower()
                    if ida.startswith('s'):
                        user_cache["Embarque na ida"] = "Sim"
                    else:
                        user_cache["Embarque na ida"] = "Não"
                    
                    
                    user_cache["Embarque na volta"] = "Não"
                    user_cache["Ponto de desembarque"] = "" 

                    screen.clear()

                    if user_cache["Embarque na ida"] == "Não":
                        cabecalho("CHECK-IN CANCELADO")
                        print("Nenhum registro foi salvo.")

                    else:
                        checkin = datetime.now()
                        checkin_formatado = checkin.strftime("%d/%m/%Y às %H:%M")


                        print(f"---INFORMAÇÕES GERAIS DO EMBARQUE---\n")

                        print(f"Check-in realizado no dia {checkin_formatado}")
                        print(f"IDA: CONFIRMADA✅")
                        print(f"Ponto de embarque: {user_cache['Ponto de embarque']}\n")
                        user_cache["Horário"] = checkin_formatado
                        print(f"STATUS VOLTA: NÃO AGENDADA/CANCELADA❌\n")

                        novo_aluno = {
                        "Nome": nome,
                        "Instituição": inst,
                        "Ponto de embarque": user_cache["Ponto de embarque"],
                        "Ponto de desembarque": "", 
                        "Embarque na ida": user_cache["Embarque na ida"],
                        "Embarque na volta": "Não",
                        "Horário": user_cache["Horário"]
                            }
                        
                        lista_atual = []
                        if os.path.exists(ARQUIVO_BANCO):
                            try:
                                with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
                                    lista_atual = json.load(arquivo)
                            except:
                                lista_atual = []

                        lista_atual.append(novo_aluno)
                        with open(ARQUIVO_BANCO, "w", encoding="utf-8") as arquivo:
                            json.dump(lista_atual, arquivo, indent=4, ensure_ascii=False)

                        input("\nPressione ENTER para voltar à página inicial...")
                        screen.clear()

                    




                        
                elif escolha_checkin == "2":
                    screen.clear()
                    cabecalho("CONFIRMAR PARTIDA (SOMENTE VOLTA)")

                    nome = input("Digite seu nome: ")
                    inst = input("Instituição: ")

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

                    volta = input(f"Deseja confirmar o embarque na VOLTA no ponto {user_cache['Ponto de desembarque']}? [s/n]: ").lower()
                    if volta.startswith('s'):
                        user_cache["Embarque na volta"] = "Sim"
                    else:
                        user_cache["Embarque na volta"] = "Não"
                    
                    
                    user_cache["Embarque na ida"] = "Não"
                    user_cache["Ponto de embarque"] = "" 

                    screen.clear()

                    if user_cache["Embarque na volta"] == "Não":
                        cabecalho("CHECK-IN CANCELADO")
                        print("Nenhum registro foi salvo.")

                    else:
                        checkin = datetime.now()
                        checkin_formatado = checkin.strftime("%d/%m/%Y às %H:%M")


                        print(f"---INFORMAÇÕES GERAIS DO EMBARQUE---\n")

                        print(f"Check-in realizado no dia {checkin_formatado}")
                        print(f"STATUS IDA: NÃO AGENDADA/CANCELADA❌\n")
                        print(f"VOLTA: CONFIRMADA✅")
                        print(f"Ponto de desembarque: {user_cache['Ponto de desembarque']}\n")
                        user_cache["Horário"] = checkin_formatado


                        novo_aluno = {
                            "Nome": nome,
                            "Instituição": inst,
                            "Ponto de embarque": "", 
                            "Ponto de desembarque": user_cache["Ponto de desembarque"],
                            "Embarque na ida": "Não",
                            "Embarque na volta": user_cache["Embarque na volta"],
                            "Horário": user_cache["Horário"]
                                 }
                        lista_atual = []
                        if os.path.exists(ARQUIVO_BANCO):
                            try:
                                with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
                                    lista_atual = json.load(arquivo)
                            except:
                                lista_atual = []
                        lista_atual.append(novo_aluno)
                        with open(ARQUIVO_BANCO, "w", encoding="utf-8") as arquivo:
                            json.dump(lista_atual, arquivo, indent=4, ensure_ascii=False)

                        input("\nPressione ENTER para voltar à página inicial...")
                        screen.clear()
                

                

                    


                    
                elif escolha_checkin == 0:
                    screen.clear()
                    paginainicial()
                    

def dadospessoais():
                with open("dados.txt", "r", encoding="utf-8") as arquivo:
                    for linha in arquivo:
                        print(linha.strip())                










            
                print()
                input("\nPressione ENTER para voltar à página inicial...")
                screen.clear()

def avisos():
                with open("avisos.txt", "r", encoding="utf-8") as arquivo:
                    for linha in arquivo:
                        print(linha.strip())
                voltar = input("\nPressione ENTER para voltar...") 
                screen.clear()               

def cancelarcheckin():
    ARQUIVO_BANCO = "banco_alunos.json"
    screen.clear()
    cabecalho("CANCELAMENTO DE CHECK-IN")
    lista_alunos = []
    if os.path.exists(ARQUIVO_BANCO):
        try:
            with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
                lista_alunos = json.load(arquivo)
        except:
            print("Erro ao ler o banco de dados.")
            return   
    if not lista_alunos:
        print("Não há nenhum check-in registrado no sistema.")
        input("\nPressione ENTER para voltar...")
        return
    
    nome_busca = input("Digite o NOME completo para buscar seu check-in: ").strip()
    aluno_encontrado = None

    for aluno in lista_alunos:
        if aluno.get("Nome", "").lower() == nome_busca.lower():
            aluno_encontrado = aluno
            break
    
    if not aluno_encontrado:
        print(f"\n❌ Check-in não encontrado para: {nome_busca}")
        input("\nPressione ENTER para voltar...")
        return

    alteracao_realizada = False 

    ida_sim = aluno_encontrado.get("Embarque na ida") == "Sim"
    volta_sim = aluno_encontrado.get("Embarque na volta") == "Sim"

    
    if ida_sim and volta_sim:
        print(f"\nOlá {aluno_encontrado['Nome']}, você tem IDA e VOLTA confirmados.")
        print(f"Horário do registro: {aluno_encontrado.get('Horário', '--')}")
        
        print("\nDeseja realizar alguma alteração?")
        print("[1] Cancelar apenas a IDA")
        print("[2] Cancelar apenas a VOLTA")
        print("[3] Cancelar AMBOS (Ida e Volta)")
        print("[0] Voltar")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            aluno_encontrado["Embarque na ida"] = "Não"
            aluno_encontrado["Ponto de embarque"] = "" 
            print("\n✅ A IDA foi cancelada. A VOLTA permanece agendada.")
            alteracao_realizada = True

        elif escolha == "2":
            aluno_encontrado["Embarque na volta"] = "Não"
            aluno_encontrado["Ponto de desembarque"] = "" 
            print("\n✅ A VOLTA foi cancelada. A IDA permanece agendada.")
            alteracao_realizada = True

        elif escolha == "3":
            lista_alunos.remove(aluno_encontrado)
            print("\n✅ IDA e VOLTA foram cancelados com sucesso.")
            alteracao_realizada = True

        elif escolha == "0":
            print("\nNenhuma alteração realizada.")

    
    elif ida_sim:
        print(f"\nOlá {aluno_encontrado['Nome']}, você tem somente IDA confirmada.")
        escolha = input("Deseja cancelar? [s/n]: ").lower()
        
        if escolha == "s":
            lista_alunos.remove(aluno_encontrado)
            print("\n✅ Check-in de IDA cancelado com sucesso!")
            alteracao_realizada = True
        else:
            print("\nMantendo check-in...")

    
    elif volta_sim:
        print(f"\nOlá {aluno_encontrado['Nome']}, você tem somente VOLTA confirmada.")
        escolha = input("Deseja cancelar? [s/n]: ").lower()
        
        if escolha == "s":
            lista_alunos.remove(aluno_encontrado)
            print("\n✅ Check-in de VOLTA cancelado com sucesso!")
            alteracao_realizada = True
        else:
            print("\nMantendo check-in...")

    else:
        print(f"\nO aluno {aluno_encontrado['Nome']} não possui embarques confirmados ativos.")
        lista_alunos.remove(aluno_encontrado)
        alteracao_realizada = True

   
    if alteracao_realizada:
        try:
            with open(ARQUIVO_BANCO, "w", encoding="utf-8") as arquivo:
                json.dump(lista_alunos, arquivo, indent=4, ensure_ascii=False)
            print("Alterações salvas no sistema.")
        except Exception as e:
            print(f"Erro ao salvar alterações: {e}")
    else:
        print("\nNenhuma alteração foi feita.")

    input("\nPressione ENTER para voltar...")
    screen.clear()

def acompanharota():
                screen.clear()
    
                with open("rota.txt", "r", encoding="utf-8") as arquivo:
                    arq = arquivo.read().splitlines()

                print(f"{'#':<3} | {'Check':<11} | {'Ponto de Parada':<25} | {'Endereço':<50}")
                print("-" * 105)

                for i in range(0, len(arq), 3):
                    check = arq[i].strip()
                    ponto = arq[i + 1].strip()
                    end = arq[i + 2].strip()

                    check_exibicao = check if check != "" else "/"

                    print(f"{i // 3 + 1:<3} | {check_exibicao:<11} | {ponto:<25} | {end:<50}")

                print()
                input("Digite ENTER para voltar...")
                screen.clear()


def ler_txt_simples(caminho):
    """Retorna uma lista de strings, sendo cada item uma linha"""
    linhas = []
    try:
        with open(caminho, 'r') as arquivo:
            for linha in arquivo:
                linhas.append(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        
    return linhas
    
def ler_txt_dicionario(caminho, separador=":"):
    """Transforma cada linha em um item de um dicionario, depois retorna o dicionario de todos os itens"""
    dicionario = {}
    try:
        with open(caminho, 'r') as arquivo:
            for linha in arquivo:
                partes = linha.split(separador, 1)
                if len(partes) != 2:
                    if linha.strip():
                        print(f"Linha invalida \"{linha.strip()}\"")
                else:
                    chave = partes[0].strip()
                    valor = partes[1].strip()
                    dicionario[chave] = valor
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        
    return dicionario

def escrever_lista(lista, caminho, separador="\n"):
    """Escreve a lista em um arquivo de texto"""
    import os

    # Garante que o diretório destino existe (se houver um diretório no caminho)
    pasta = os.path.dirname(caminho) or "."
    os.makedirs(pasta, exist_ok=True)

    # Converte itens para string e escreve usando o separador fornecido
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(separador.join(str(item) for item in lista))
    
def escrever_dicionario(dicionario, caminho, separador_dic=";", separador_lista="\n"):
    """Escreve o dicionario em um arquivo de texto"""
    # Transforma o dicionário em uma lista
    lista = [f"{chave}{separador_dic}{valor}" for chave, valor in dicionario.items()]
    # Escreve essa lista
    escrever_lista(lista, caminho, separador=separador_lista)

def carregar_user_cache(caminho_arquivo):
    user_cache = {
        "Ponto de embarque": "",
        "Embarque na ida": "Não",
        "Ponto de desembarque": "",
        "Embarque na volta": "Não",
        "Horário": "",
    }

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if not linha or ":" not in linha:
                continue

            chave, valor = linha.split(":", 1)
            chave = chave.strip()
            valor = valor.strip()

            if chave in user_cache:
                user_cache[chave] = valor

    return user_cache





















#motoristas

