def PasswordReset(email):
    from random import randint
    logins = open("logins.txt")
    linhas = logins.read().splitlines()
    logins.close()

    if email in linhas:
        codigo_reset = f"{randint(0, 999):03}"

        reset = open("codigo.txt", "w")
        reset.write(codigo_reset + "\n")
        reset.close()

        reset = open("codigo.txt", "r")
        codigoreset = reset.read().splitlines()
        reset.close()
        
        print("Se esse email estiver cadastrado, ensira o código que foi enviado")
        codigo = input("Digite o código de reset: ")

        if codigo == codigoreset[0]:
            posicao_senha = linhas.index(email)+1
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


def CreateNotice():
    from datetime import datetime
    while True:
        print("Digite o Aviso [SAIR para encerrar]:")
        text = str(input("-> "))
        if text.upper() == 'SAIR':
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


from time import sleep

def carregar_universidades():
    
    import os
    lista_universidades = []

    # Verifica existência do arquivo
    if not os.path.exists("lista_universidades.txt"):
        return lista_universidades

    # Lê o conteúdo
    with open("lista_universidades.txt", "r") as f:
        conteudo = f.read().strip()

    # Arquivo vazio → lista vazia
    if not conteudo:
        return lista_universidades

    # Divide em blocos
    blocos = conteudo.split("---")

    for bloco in blocos:
        linhas = [x.strip() for x in bloco.splitlines() if x.strip()]
        if len(linhas) >= 3:
            lista_universidades.append({
                "nome": linhas[0],
                "cnpj": linhas[1],
                "endereco": linhas[2]
            })

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
        "endereco": endereco
    })

    salvar_universidades(lista_universidades)

    print(f"\n:Universidade '{nome}' cadastrada com sucesso!")
    sleep(2)


def listar_universidades():
    lista_universidades = carregar_universidades()

    print("\n=== UNIVERSIDADES CADASTRADAS ===\n")

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

    # Verifica se é número
    if not entrada.isdigit():
        print("Entrada inválida.")
        sleep(2)
        return

    i = int(entrada) - 1

    # Verifica intervalo
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
        "endereco": novo_endereco
    }

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

    # Verifica se é número
    if not entrada.isdigit():
        print("Entrada inválida.")
        sleep(2)
        return

    i = int(entrada) - 1

    # Valida intervalo
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

def Editar_usuário(tipo_de_usuario_editado):
    alteracao_aluno = False
    alteracao_motoristas = False
    from time import sleep
    with open("logins.txt", "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()
        linhas_limpa = [linha for linha in linhas if linha != ""]
        alunos = []
        motoristas = []

        for c, linha in enumerate(linhas_limpa):
            if linha=='aluno':
                alunos.append(linhas_limpa[c:c+11])
            if linha=='motorista':
                motoristas.append(linhas_limpa [c:c+8])

    if tipo_de_usuario_editado=='aluno':            
        if not alunos:
            print("Não há nenhum aluno cadastrados!")
        else:
            print("\nAlunos cadastrados:")
        for i, aluno in enumerate(alunos):
            nome = aluno[3]
            print(f"[{i+1}] - {nome}")

        indice = int(input("\nDigite o número do aluno que deseja editar: "))-1
        aluno = alunos[indice]

        cpf_formatado=f"{aluno[7][:3]}.{aluno[7][3:6]}.{aluno[7][6:9]}-{aluno[7][9:]}"
        telefone_formatado=f"({aluno[8][:2]}){aluno[8][2:7]}-{aluno[8][7:]}"
        data_formatada=f"{aluno[9][:2]}/{aluno[9][2:4]}/{aluno[9][4:]}"

        print("\nInformações atuais:")
        print(f'''1 - Nome: {aluno[3]}
2 - Instituição: {aluno[4]}
3 - Ponto de embarque: {aluno[5]}
4 - Ponto de desembarque: {aluno[6]}
5 - Cpf: {cpf_formatado}
6 - Telefone: {telefone_formatado}
7 - Data de nascimento {data_formatada}''')

        campo=0
        lista=["nome", "Instituição", "Ponto de Embarque", "Ponto de Desembarque", "Cpf", "Telefone", "Data de nascimento" ]
        while True:
            try:
                campo = int(input("\nQual campo deseja editar (1-7)? "))
                if 1 <= campo <= 7:
                    novo_valor = input(f"Digite o novo valor para {aluno[campo-1]}: ")
                    aluno[campo + 2] = novo_valor
                    alunos[indice] = aluno
                    alteracao_aluno = True
                    break
                else: 
                    print("Por favor insira um número entre 1 e 7!")
            except ValueError:
                print("Por favor digite um número inteiro válido!")

    if tipo_de_usuario_editado=='motorista':            
        if not motoristas:
            print("Não há nenhum motorista cadastrados!")
        else:
            print("\nMotoristas cadastrados:")
        for i, motorista in enumerate(motoristas):
            nome = motorista[3]
            print(f"[{i+1}] - {nome}")

        indice = int(input("\nDigite o número do motorista que deseja editar: "))-1
        motorista = motoristas[indice]

        cpf_formatado=f"{motorista[4][:3]}.{motorista[4][3:6]}.{motorista[4][6:9]}-{motorista[4][9:]}"
        telefone_formatado=f"({motorista[5][:2]}){motorista[5][2:7]}-{motorista[5][7:]}"
        data_formatada=f"{motorista[6][:2]}/{motorista[6][2:4]}/{motorista[6][4:]}"

        print("\nInformações atuais:")
        print(f'''1 - Nome: {motorista[3]}
2 - Cpf: {cpf_formatado}
3 - Telefone: {telefone_formatado}
4 - Data de Nascimento {data_formatada}''')
        
        while True:
            try:
                campo = int(input("\nQual campo deseja editar (1-4)? "))

                if 1 <= campo <= 4:
                    novo_valor = input(f"Digite o novo valor para {motorista[campo-1]}: ")
                    motorista[campo + 2] = novo_valor
                    motoristas[indice] = motorista
                    alteracao_motoristas = True
                    break
                else: 
                    print("Por favor insira um número entre 1 e 4!")
            except ValueError:
                print("Por favor digite um número inteiro válido!")

    if alteracao_aluno:
        inicio = linhas_limpa.index(aluno[0])
        linhas_limpa[inicio:inicio+len(aluno)] = aluno

        with open("logins.txt", "w", encoding="utf-8") as f:
            for i, linha in enumerate(linhas_limpa):
                f.write(linha + "\n")
                if linha =="-":
                    f.write("\n")

            print("\nInformação atualizada com sucesso!")
        sleep(3)

    if alteracao_motoristas:
        inicio = linhas_limpa.index(motorista[0])
        linhas_limpa[inicio:inicio+len(motorista)] = motorista

        with open("logins.txt", "w", encoding="utf-8") as f:
            for i, linha in enumerate(linhas_limpa):
                f.write(linha + "\n")
                if linha =="-":
                    f.write("\n")


        print("\nInformação atualizada com sucesso!")
        sleep(3)

def Adicionar_usuario(tipo_de_usuário_adicionado):

    adicao_aluno=False
    adicao_motorista=False

    with open("logins.txt", "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()
        linhas_limpa = [linha for linha in linhas if linha != ""]
        alunos = []
        motoristas = []

    lista=["nome", "Instituição", "Ponto de Embarque", "Ponto de Desembarque", "Cpf", "Telefone", "Data de nascimento" ]
    
    if tipo_de_usuário_adicionado=='aluno':
        for posição in linhas_limpa:
            posição=="motorista"
            indice=linhas_limpa.index(posição)

        novo_usuario=[]
        novo_usuario.append("aluno")
        email=input("Digite o email do aluno: ")
        novo_usuario.append(email)
        novo_usuario.append("aluno123")
        nome=input("Digite o nome do aluno: ")
        novo_usuario.append(nome)
        Instituição=input("Digite a instituição do aluno: ")
        novo_usuario.append(Instituição)
        Ponto_de_Embarque=input("Digite o ponto de embarque do aluno: ")
        novo_usuario.append(Ponto_de_Embarque)
        Ponto_de_Desembarque=input("Digite o ponto de desembarque do aluno: ")
        novo_usuario.append(Ponto_de_Desembarque)
        Cpf=input("Digite o cpf do aluno: ")
        novo_usuario.append(Cpf)
        Telefone=input("Digite o telefone do aluno: ")
        novo_usuario.append(Telefone)
        Data_de_nascimento=input("Digte a data de nascimento do aluno: ")
        novo_usuario.append(Data_de_nascimento)
        novo_usuario.append("-")
        adicao_aluno=True

    elif tipo_de_usuário_adicionado=="motorista":

        novo_usuario=[]
        novo_usuario.append("motorista")
        email=input("Digite o email do motorista")
        novo_usuario.append(email)
        novo_usuario.append("moto123")
        nome=input("Digite o nome do motorista: ")
        novo_usuario.append(nome)
        Cpf=input("Digite o cpf do motorista: ")
        novo_usuario.append(Cpf)
        Telefone=input("Digite o cpf do motorista: ")
        novo_usuario.append(Cpf)
        Data_de_nascimento("Digite a da nascimento do motorista: ")
        novo_usuario.append(Data_de_nascimento)
        novo_usuario.append("-")
        adicao_motorista=True

    linhas_limpa.extend(novo_usuario)

    if adicao_aluno:
        with open("logins.txt", "w", encoding="utf-8") as f:
            for i, linha in enumerate(linhas_limpa):
                f.write(linha + "\n")
                if linha =="-":
                    f.write("\n")

    if adicao_motorista:
        with open("logins.txt", "w", encoding="utf-8") as f:
            for i, linha in enumerate(linhas_limpa):
                f.write(linha + "\n")
                if linha =="-":
                    f.write("\n")
                    
def Sua_conta(tipo_de_login):
    from random import randint
    with open ("logins.txt", "r+", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines()]
        
        indície=linhas.index(tipo_de_login)
        print(f'''
    Login {tipo_de_login}

Nome: {linhas[indície+3]}
Data de Nascimento: {linhas[indície+6]}
Cpf: {linhas[indície+4]}
Telefone: {linhas[indície+5]}
              ''')
        while True:
            opc=int(input('''
[1] Alterar Telefone
[0] Voltar: 
                    
Digite: '''))
            
            if opc==1:
                print("O código de acesso foi enviado para seu número")
                codigo_reset = f"{randint(0, 999999):06}"

                with open("codigo.txt", "w", encoding="utf-8") as reset:
                    reset.write(codigo_reset + "\n")

                with open("codigo.txt", "r", encoding="utf-8") as reset:
                    codigoreset = reset.read().strip() 
                
                codigo=input("Digte: ")
                if codigo == codigoreset:
                    linhas[indície + 5] = input("Digite seu novo telefone: ")
                
                    with open("logins.txt", "w", encoding="utf-8") as logins:
                        logins.writelines([linha + "\n" for linha in linhas])

                    print("Telefone alteraqdo com sucesso! ")
                else:
                    print("Codigo incorreto! ")
            elif opc==0:
                break

def Credenciais(tipo_de_login):
    with open ("logins.txt", "r+", encoding="utf-8") as f:
        linhas = [linha.strip() for linha in f.readlines()]
        
        indície=linhas.index(tipo_de_login)

        senha=linhas[indície+2]
        while True:
            confirmar_senha=input("Por favor insira sua senha para entrar neste campo: ")
            if confirmar_senha==senha:
                print(f"Senha atual: {senha}")
                opc=int(input('''
[1] Alterar senha
[0] Voltar

Digite: '''))
                if opc==1:
                    PasswordReset(linhas[indície+1])
                if opc==0:
                    break
            else:
                print("Senha incorreta! ")
