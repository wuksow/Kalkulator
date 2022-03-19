number0 = input("Podaj pierwsza liczbe! ")
number1 = input("Podaj druga liczbe! ")

if not number0.isdigit() or not number1.isdigit():
    print("Podaj poprawnie liczby! ")
    exit()

number0 = int(number0)
number1 = int(number1)

typeslista = ["+", "-", "*", "%", "/", "//"]
print("Typy:", typeslista)
typ = input("Podaj typ dzialania! ")

def get_wynik(typ, liczba1, liczba2):
    switch = {
        "+": liczba1 + liczba2,
        "-": liczba1 - liczba2,
        "*": liczba1 * liczba2,
        "%": liczba1 % liczba2,
        "/": liczba1 / liczba2,
        "//": liczba1 // liczba2
    }
    return switch.get(typ, "Nie ma takiego typu!")

print("Wynik to", get_wynik(typ, number0, number1))