#!/usr/bin/python
# -*- coding: utf-8 -*-

# Wprowadzenie do Informatyki (Moduł 1)
# Temat: 9. Zaprogramuj w języku Python (002) program typu przelicznik, który pozwala na przeliczanie
# stopni celsiusa na stopnie Fahrenheita i na odwrót lub kalkulator walutowy, który pozwala
# na przeliczenie cebulionów na v-dolary). W tym ostatnim przypadku można opcjonalnie
# rozszerzyć funkcjonalność programu o pobieranie danych z zewnętrznych źródeł (np.
# aktualny kurs dolara), ale na początek wystarczy wpisać obecną wartość z tabeli kursów NBP).

# Authors: Jakub Sydor <jakusyd988@student.polsl.pl>, Przemysław Nowak <przenow638@student.polsl.pl>

import re
import os


def fahrenheit_to_celsius(value: float) -> float:
    """
    returns round((value - 32) / 1.8, 2)

    Convert fahrenheit degrees to celsius degrees. Up to 2 point over zero.

        :param value: fahrenheit degrees
        :type value: float
        :returns: celsius value
        :rtype: float

        :Example:

            >>> a = fahrenheit_to_celsius(0)
            >>> print(a)
            -17.78
    """
    return round((value - 32) / 1.8, 2)


def celsius_to_fahrenheit(value: float) -> float:
    """
    returns round((value * 1.8) + 32, 2)

    Convert celsius degrees to fahrenheit degrees. Up to 2 point over zero.

        :param value: celsius degrees
        :type value: float
        :returns: fahrenheit value
        :rtype: float

        :Example:

            >>> a = celsius_to_fahrenheit(-17.78)
            >>> print(a)
            0.0
    """
    return round((value * 1.8) + 32, 2)


def format_temp_unit(value: float, unit: str) -> str:
    """
    returns formatted degrees value

    Format celsius or fahrenheit degrees to nice string output.

        :param value: celsius or fahrenheit degrees value
        :param unit: 'C' for celsius or 'F' for fahrenheit degrees
        :type value: float
        :type unit: str
        :returns: value with degrees symbol
        :rtype: str

        :Example:

            >>> a = format_temp_unit(-17.78, 'c')
            >>> print(a)
            "-17.78℃"
    """
    if unit.lower() == 'c':
        return f"{value}℃"
    elif unit.lower() == 'f':
        return f"{value}℉"
    else:
        return str(value)


def get_user_input() -> float:
    """
     returns user input

     Get user input from console. Check if match float type. Convert to float type and return

         :returns: user input
         :rtype: float

         :Example:

             >>> a = get_user_input()
             Podaj wartość: 12.3
             >>> print(a)
             12.3
     """
    while 1:
        val = input("Podaj wartość: ")
        if re.match('[+-]?([0-9]*[.])?[0-9]+', val):
            return float(val)
        else:
            print(f"Wartość '{val}', musi byc typu float")


def app_menu():
    os.system("cls")
    print("Wprowadzenie do Informatyki (Moduł 1)")
    print("     by Jakub Sydor, Przemysław Nowak")
    print("")
    print("  Wybór opcji:  ")
    print("    1: celcjusz -> fahrenheit  ")
    print("    2: fahrenheit -> celcjusz  ")
    print("    q: wyjście  ")
    choose = input("Twój wybór: ")

    a = get_user_input()

    if choose == '1':
        print(f"{format_temp_unit(a, 'c')} jest to {format_temp_unit(celsius_to_fahrenheit(a), 'f')}")
    elif choose == '2':
        print(f"{format_temp_unit(a, 'f')} jest to {format_temp_unit(fahrenheit_to_celsius(a), 'c')}")
    elif choose == 'q':
        return 0
    else:
        print('Wartość menu nieznana')

    print()
    print("Kliknij enter, aby móc dalej przeliczać...")
    input()
    return app_menu()


if __name__ == '__main__':
    app_menu()
