def kalkulator():
    try:
        num1 = int(input("Podaj liczbę 1: "))
        num2 = int(input("Podaj liczbę 2: "))
    except ValueError:
        print("Nie podano liczb")
        return

    operacja = input("Podaj operacje (+, -, *, /): ")

    if operacja == "+":
        print(num1 + num2)
    elif operacja == "-":
        print(num1 - num2)
    elif operacja == "*":
        print(num1 * num2)
    elif operacja == "/":
        print(num1 / num2)
    else:
        print("Wystąpił błąd upewnij się że podane dane są poprawne")

def main():
    choice = input("Wybierz podzadanie")
    match choice:
        case '1':
            kalkulator()
        case _:
            print("Nie podano liczb podzadania")

if __name__ == '__main__':
    main()

