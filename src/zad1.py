paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Ilosc paliwa [l]: {paliwo}")
    paliwo -= paliwo_zuzyte_na_s
    czas +=1
else:
    print(f"Koniec lotu. Czas lotu: {czas}s")