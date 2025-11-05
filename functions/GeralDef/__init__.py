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

