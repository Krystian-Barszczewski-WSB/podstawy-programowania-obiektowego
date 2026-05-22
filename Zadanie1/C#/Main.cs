using System;

public class Program
{
	static void Kalkulator()
	{
		try
		{
			Console.Write("Podaj liczbę 1: ");
			int num1 = int.Parse(Console.ReadLine());

			Console.Write("Podaj liczbę 2: ");
			int num2 = int.Parse(Console.ReadLine());

			Console.Write("Podaj operacje (+, -, *, /): ");
			string operacja = Console.ReadLine();

			if (operacja == "+")
				Console.WriteLine(num1 + num2);
			else if (operacja == "-")
				Console.WriteLine(num1 - num2);
			else if (operacja == "*")
				Console.WriteLine(num1 * num2);
			else if (operacja == "/")
			{
				if (num2 == 0)
				{
					Console.WriteLine("Błąd: Dzielenie przez zero");
					return;
				}
				
				Console.WriteLine((double)num1 / num2); 
			}
			else
				Console.WriteLine("Błąd: Upewnij się że podane dane są poprawne");
		}
		catch (FormatException)
		{
			Console.WriteLine("Błąd: Podano niepoprawne wartości");
		}
	}

	static void KonwerterTemperatur()
	{
		try
		{
			Console.Write("Podaj z jakiego systemu konwertujesz(C/F): ");
			string konwersja = Console.ReadLine();

			Console.Write("Podaj temperature: ");
			int temperatura = int.Parse(Console.ReadLine());

			if (konwersja == "C" || konwersja == "c")
			{
				double wynik = Math.Round((temperatura * 1.8) + 32, 2);
				Console.WriteLine($"{wynik} F*");
			}
			else
			{
				double wynik = Math.Round((temperatura - 32) / 1.8, 2);
				Console.WriteLine($"{wynik} C*");
			}
		}
		catch (FormatException)
		{
			Console.WriteLine("Błąd: Podano niepoprawne wartości");
		}
	}

	static void SredniaOcen()
	{
		try
		{
			Console.Write("Podaj ilość wprowadzanych ocen: ");
			int iloscOcen = int.Parse(Console.ReadLine());

			double srednia = 0;

			for (int x = 0; x < iloscOcen; x++)
			{
				int ocena = 0;
				while (ocena <= 0 || ocena > 6)
				{
					Console.Write($"Podaj ocene(1-6) nr {x + 1}: ");
					ocena = int.Parse(Console.ReadLine());
				}
				srednia += ocena;
			}

			srednia /= iloscOcen;
			Console.WriteLine($"Średnia wynosi: {Math.Round(srednia, 2)}");

			if (srednia >= 3)
				Console.WriteLine("Uczeń zdał.");
			else
				Console.WriteLine("Uczeń nie zdał");
		}
		catch (FormatException)
		{
			Console.WriteLine("Błąd: Podano niepoprawne wartości");
		}
	}

	public static void Main()
	{
	    while (true)
	    {
            Console.Write("Wybierz podzadanie(1 - kalkulator, 2 - konwersja temperatur, 3 - srednia ocen, x - wyjscie z programu): ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Kalkulator();
                    break;
                case "2":
                    KonwerterTemperatur();
                    break;
                case "3":
                    SredniaOcen();
                    break;
                case "x":
                case "X":
                    return;
                default:
                    Console.WriteLine("Nie podano numeru podzadania");
                    break;
            }
        }
	}
}