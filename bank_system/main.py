import os
VERMELHO = "\033[31m"
AMARELO = A = "\033[33m"
VERDE = "\033[32m"
AZUL = "\033[34m"
NEGRITO = N = "\033[1m"
FUNDO_AZUL = FA= "\033[44m"

RESET_COR = R = "\033[0m"
OI = f"{AZUL}Olá, seja bem vindo ao Banco Python!{RESET_COR}"

def letras_menu (letra: str):
    return f"{N}{A}{FA}[{letra}]{R}{RESET_COR}"
MENU = f"""
{AMARELO}---- MENU ----{RESET_COR}
{letras_menu('d')} Depositar
{letras_menu('s')} Sacar
{letras_menu('e')} Extrato
{letras_menu('q')} Sair
{OI}
=> """
senha = None
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def clear():
    my_print("")
    
def my_print(msg: str):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print(msg)

while True:
    operacao = input(MENU)

    match operacao:
        case "d":
            clear()
            valor = float(input(f"{AMARELO}Informe o valor do depósito: R${RESET_COR}"))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")
        

        case "s" | "S":
            clear()
            valor = float(input(f"{AMARELO}Informe o valor do saque: R${RESET_COR}"))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                my_print(f"{VERMELHO}Operação falhou! Saldo insuficiente suficiente.{RESET_COR}")

            elif excedeu_limite:
                my_print(f"{VERMELHO}Operação falhou! Você excedeu o valor limite de saque diários.{RESET_COR}")

            elif excedeu_saques:
                my_print(f"{VERMELHO}Operação falhou! Você atingiu o número máximo de saques.{RESET_COR}")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                my_print(f"{VERDE}Saque realizado com sucesso!{RESET_COR}")

            else:
                my_print(f"{VERMELHO}Operação falhou! Valor inválido.{RESET_COR}")

        case "e" | "E":
            clear()
            print(AMARELO + "EXTRATO".center(50, "="))
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("FIM".center(50, "=") + RESET_COR)

        case "q" | "Q":
            break

        case _:
            my_print("Operação inválida, por favor selecione uma das opções disponíveis no menu.")