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


