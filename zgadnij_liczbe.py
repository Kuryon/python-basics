import random

random_liczba = random.randint(1, 100)
ilosc_trafien = 0

while True:
    zgadywanie = int(input("Zgadnij jaka to liczba (0-100): "))
    if zgadywanie == random_liczba:
        print(f"Zgadles w {ilosc_trafien} próbach!")
        pytanie = input("Chcesz zagrać jeszcze raz? (Tak/Nie): ")
        ilosc_trafien = 0
        if pytanie == "Nie":
            break
    elif zgadywanie > random_liczba:
        print("Za dużo")
        ilosc_trafien += 1
    elif zgadywanie < random_liczba:
        print("Za mało")
        ilosc_trafien += 1
    else:
        print("Napisz poprawną liczbę")