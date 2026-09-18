from random import randint


def main():
    while True:
        operador = getoperator()
        if operador == 5:
            return
        level = getlevel()
        if operador == 1:  # soma
            x = geradornumero(level, 0)
            y = geradornumero(level, 0)
            print(f"{x} + {y}")
            answer = x + y
            while True:
                try:
                    user_answer = int(input("Resposta: "))
                    if user_answer == answer:
                        print("Correto\n")
                        break
                    else:
                        print("Errado")
                        continue
                except ValueError:
                    pass

        elif operador == 2:  # subtração
            x = geradornumero(level, 0)
            y = geradornumero(level, x)
            print(f"{x} - {y}")
            answer = x - y
            while True:
                try:
                    user_answer = int(input("Resposta:"))
                    if user_answer == answer:
                        print("Correto\n")
                        break
                    else:
                        print("Errado")
                        continue
                except ValueError:
                    pass

        elif operador == 3:  # multiplicação
            x = geradornumero(level, 0)
            y = geradornumero(1, 0)
            print(f"{x} * {y}")
            answer = x * y
            while True:
                try:
                    user_answer = int(input("Resposta"))
                    if user_answer == answer:
                        print("Correto\n")
                        break
                    else:
                        print("Errado")
                        continue
                except ValueError:
                    pass

        elif operador == 4:  # Divisão
            x = geradornumero(level, 0)
            y = geradornumero(1, 1)
            print(f"{x}/{y}")
            answer = x / y
            while True:
                try:
                    user_answer = int(input("Resposta"))
                    if user_answer == answer:
                        print("Correto\n")
                        break
                    else:
                        print("Errado")
                        continue
                except ValueError:
                    pass


def getoperator():
    print("=" * 25)
    print(
        "[1] Soma(+)\n[2] Subtração(-)\n[3] Multiplicação(*)\n"
        "[4] Divisão(/)\n[5]Exit"
    )
    print("=" * 25)
    while True:
        try:
            operador = int(input("Escolha um operador: "))
            return operador
        except ValueError:
            pass


def getlevel():
    while True:
        try:
            level = int(input("Select level (1, 2 or 3): "))
            if 0 < level <= 3:
                return level
            else:
                continue
        except ValueError:
            pass


def geradornumero(level, cap):
    if level == 1:
        return randint(cap, 9)
    elif level == 2:
        return randint(cap, 99)
    elif level == 3:
        return randint(cap, 999)


if __name__ == "__main__":
    main()
