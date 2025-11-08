from time import sleep

def carregar_universidades():
    lista_universidades = []
    try:
        with open("lista_universidades.txt", "r") as f:
            conteudo = f.read().strip()
            if conteudo:
                blocos = conteudo.split("---")
                for bloco in blocos:
                    linhas = [x.strip() for x in bloco.splitlines() if x.strip()]
                    if len(linhas) >= 3:
                        lista_universidades.append({
                            "nome": linhas[0],
                            "cnpj": linhas[1],
                            "endereco": linhas[2]
                        })
    except FileNotFoundError:
        pass
    return lista_universidades


def salvar_universidades(lista_universidades):
    with open("lista_universidades.txt", "w") as f:
        for u in lista_universidades:
            f.write(f"{u['nome']}\n{u['cnpj']}\n{u['endereco']}\n---\n")


def cadastrar_universidade():
    nome = input("Nome: ").strip()
    cnpj = input("CNPJ: ").strip()
    endereco = input("Endereço: ").strip()
    if nome and cnpj and endereco:
        lista_universidades = carregar_universidades()
        lista_universidades.append({"nome": nome, "cnpj": cnpj, "endereco": endereco})
        salvar_universidades(lista_universidades)
        print(f"\n✅ Universidade '{nome}' cadastrada com sucesso!")
    else:
        print("❌ Todos os campos são obrigatórios.")
    sleep(2)


def listar_universidades():
    lista_universidades = carregar_universidades()
    print("\n=== UNIVERSIDADES CADASTRADAS ===\n")
    if not lista_universidades:
        print("Nenhuma universidade cadastrada.")
    else:
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
    try:
        i = int(input("\nDigite o número da universidade: ")) - 1
        if 0 <= i < len(lista_universidades):
            u = lista_universidades[i]
            novo_nome = input(f"Novo nome ({u['nome']}): ").strip() or u['nome']
            novo_cnpj = input(f"Novo CNPJ ({u['cnpj']}): ").strip() or u['cnpj']
            novo_endereco = input(f"Novo Endereço ({u['endereco']}): ").strip() or u['endereco']
            lista_universidades[i] = {"nome": novo_nome, "cnpj": novo_cnpj, "endereco": novo_endereco}
            salvar_universidades(lista_universidades)
            print("✅ Universidade atualizada com sucesso!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")
    sleep(2)


def excluir_universidade():
    lista_universidades = carregar_universidades()
    if not lista_universidades:
        print("Nenhuma universidade cadastrada.")
        sleep(2)
        return

    listar_universidades()
    try:
        i = int(input("\nDigite o número para excluir: ")) - 1
        if 0 <= i < len(lista_universidades):
            confirm = input(f"Excluir '{lista_universidades[i]['nome']}'? (s/n): ").lower()
            if confirm == "s":
                nome = lista_universidades[i]["nome"]
                del lista_universidades[i]
                salvar_universidades(lista_universidades)
                print(f"✅ '{nome}' excluída com sucesso!")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")
    sleep(2)
