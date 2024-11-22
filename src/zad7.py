liczba_studentow = int(input("Podaj liczbe studentów:"))
suma_punktow = 0
liczba_odczytow=0

for i in range(0, liczba_studentow):
    liczba_punktow = int(input("Podaj liczbe punktow"))
    if(liczba_punktow < 0 or liczba_punktow >100):
        continue
    else:
        liczba_odczytow +=1
        suma_punktow += liczba_punktow
print(f"Liczba poprawnych odczytow: {liczba_odczytow}")
print(f"Średnia liczba punktów: {suma_punktow/liczba_odczytow}")