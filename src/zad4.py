liczba_gosci = int(input("Podaj liczbe gości"))
liczba_potraw = int(input("Podaj liczbe potraw"))

suma = 0
i = 0
while i < liczba_potraw:
    suma += float(input(f"Podaj cene potrway nr {i + 1}: "))
    i +=1

srednia_cena = suma/ liczba_potraw

print(f"Każdy powinien zapłacić : {suma/liczba_gosci}")