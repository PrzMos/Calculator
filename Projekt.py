#!/usr/bin/env python
# -*- coding: utf-8 -*-
print
"....:::::KALKULATOR::::...."
print("Witaj oto jest mój Kalkulator!")


def menu():
    print ("::MENU::\n"
        "1 - dodawanie\n"
        "2 - odejmowanie\n"
        "3 - mnożenie\n"
        "4 - dzielenie\n"
        "5 - dzielenie całkowite\n"
        "6 - potęgowanie\n"
        "7 - delta\n"
        "8 - autor\n"
        "9 - o programie\n"
        "10 - koniec\n"  
        "0 - MENU\n")



def dodawanie():
    print("Wybrałeś dodawanie!")
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    wynik = float(a) + float(b)
    print("wynik", wynik)
    return wynik


def odejmowanie():
    print("Wybrałeś odejmowanie!")
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    wynik = float(a) - float(b)
    print("wynik", wynik)
    return wynik


def mnozenie():
    print("Wybrałeś mnożenie")
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    wynik = float(a) * float(b)
    print("wynik", wynik)
    return wynik


def dzielenie():
    print("Wybrałeś dzielenie!")
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    if (float(b) == 0): print("Nie można dzielić przez 0!")
    wynik = float(a) / float(b)
    print("Wynik",wynik)

    return wynik


def dzieleniecal():
    print("Wybrałeś dzielenie całkowite!")
    a = input("Pierwsza liczba ")
    b = input("Druga liczba ")
    reszta = int(a) % int(b)
    c = int(a) - reszta
    dziel = int(c) / int(b)
    wynik = "wynik", dziel, "reszty", reszta
    print("Wynik", dziel, "reszta", reszta)
    return wynik


def potegowanie():
    print("Wybrałeś potęgowanie")
    a = input("Liczba ")
    b = input("Potęga ")
    wynik = float(a) ** float(b)
    print("wynik", wynik)
    return wynik

def delta():
    print("Wybrałeś obliczanie delty")
    a = input("Liczba a: ")
    b = input("Liczba b: ")
    c = input("Liczba c: ")
    wynik = int(b)*int(b)-4*int(a)*int(c)
    print("wynik", wynik)
    return wynik

def autor():
    print("Autor" )
    wynik = "Przemysław Mosurek student studiów Niestacjonarnych Informatyka i Ekonometria Rok 1."
    print(wynik)
    return wynik


def program():
    wynik = "Program Kalkulator który zawiera podstawowe działania na liczbach."
    print(wynik)
    return wynik


def blad():
    return 'Error'


def zakoncz():
    return 'koniec'


# Wyswietlanie

menu()

funkcje = {'1': dodawanie, '2': odejmowanie, '3': mnozenie, '4': dzielenie, '5': dzieleniecal, '6': potegowanie,
           '8': autor, '9': program, '10': zakoncz, '7':delta, '0': menu}
nazwyFunkcji = {'1': 'dodawanie', '2': 'odejmowanie', '3': 'mnożenie', '4': 'dzielenie', '5': 'dzielenie całkowite',
                '6': 'potęgowanie', '8': 'autor', '9': 'o programie', '10': 'zakończ', '7':'delta', '0': 'menu'}

operacja = input("Co wybierzesz ? ")
while operacja != "10":
    wybranaFkcja = funkcje.get(operacja, blad)
    nazwaWybranejFkcji = nazwyFunkcji.get(operacja, blad)
    print
    ":::wybrales {nazwa}::::\n {wynik}".format(nazwa=nazwaWybranejFkcji, wynik=wybranaFkcja())
    operacja = input("Co wybierzesz ? ")