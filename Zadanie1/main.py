def kalkulator():
    try:
        num1 = int(input("Podaj liczbę 1: "))
        num2 = int(input("Podaj liczbę 2: "))
        operacja = input("Podaj operacje (+, -, *, /): ")
    except ValueError:
        print("Błąd: Podano niepoprawne wartośći")
        return

    if operacja == "+":
        print(num1 + num2)
    elif operacja == "-":
        print(num1 - num2)
    elif operacja == "*":
        print(num1 * num2)
    elif operacja == "/":
        if num2 == 0:
            print("Błąd: Dzielenie przez zero")
            return
        print(round(num1 / num2, 2))
    else:
        print("Błąd: Upewnij się że podane dane są poprawne")

def konwerter_temperatur():
    try:
        konwersja = input("Podaj z jakiego systemu konwertujesz(C/F): ")
        temperatura = int(input("Podaj temperature: "))
    except ValueError:
        print("Błąd: Podano niepoprawne wartości")
        return

    if konwersja == "C" or konwersja == "c":
        print(str(round((temperatura * 1.8) + 32, 2)) + " F*")
    else:
        print(str(round((temperatura - 32) / 1.8, 2)) + " C*")

def srednia_ocen():
    try:
        ilosc_ocen = int(input("Podaj ilość wprowadzanych ocen: "))
    except ValueError:
        print("Błąd: Podano niepoprawne wartości")
        return

    srednia = 0

    for x in range(ilosc_ocen):
        try:
            ocena = 0
            while ocena <= 0 or ocena > 6:
                ocena = int(input("Podaj ocene(1-6) nr " + str(x + 1) + ": "))
            srednia += ocena
        except ValueError:
            print("Błąd: Nie podano liczby")
            return

    srednia /= ilosc_ocen

    print("Średnia wynosi: " + str(round(srednia,2)))
    if srednia >= 3:
        print("Uczeń zdał.")
    else:
        print("Uczeń nie zdał")

def main():
    choice = input("Wybierz podzadanie(1 - kalkulator, 2 - konwersja tmeperatur, 3 - srednia ocen, x - wyjscie z programu): ")
    match choice:
        case '1':
            kalkulator()
        case '2':
            konwerter_temperatur()
        case '3':
            srednia_ocen()
        case 'x':
            return
        case 'X':
            return
        case _:
            print("Nie podano numeru podzadania")
    main()

if __name__ == '__main__':
    main()

