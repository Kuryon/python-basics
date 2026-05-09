def oblicz_bmi(waga, wzrost):
    return waga / (wzrost ** 2)

def ocen_bmi(bmi):
    if bmi >= 17.0 and bmi <= 18.5:
        return "Niedowaga"
    elif bmi > 18.5 and bmi <= 24.9:
        return "Normalna waga"
    elif bmi >= 25 and bmi <= 29.9:
        return "Nadwaga"
    elif bmi > 30:
        return "Otyłość"
    else:
        return "Poza skalą"

def main():
    waga = float(input("Ile ważysz (kg)?: "))
    wzrost = float(input("Ile masz wzrostu (m)?: "))

    wynik = oblicz_bmi(waga, wzrost)
    print(wynik)

    ocen_bmi(wynik)

main()