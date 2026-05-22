def kalkulator():
    try:
        num1 = int(input("Podaj liczbę 1: "))
        num2 = int(input("Podaj liczbę 2: "))
        operacja = input("Podaj operacje (+, -, *, /): ")
    except ValueError:
        print("Podano błędne wartośći")
        return

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

def konwerterTemperatur():
    try:
        konwersja = input("Podaj z jakiego systemu konwertujesz(C/F): ")
        temperatura = int(input("Podaj temperature: "))
    except ValueError:
        print("Podano błędne wartości")
        return

    if konwersja == "C" or konwersja == "c":
        print(str(round((temperatura * 1.8) + 32, 2)) + " F*")
    else:
        print(str(round((temperatura - 32) / 1.8, 2)) + " C*")

def main():
    choice = input("Wybierz podzadanie: ")
    match choice:
        case '1':
            kalkulator()
        case '2':
            konwerterTemperatur()
        case _:
            print("Nie podano liczb podzadania")

if __name__ == '__main__':
    main()

