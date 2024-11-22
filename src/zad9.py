imie = input("Podaj imie")
wiek = int(input("Podaj wiek"))
nazwisko = input("Podaj nazwisko")
lancuch = input("Podaj lancuch")
lancuch2 = input("Podaj drugi lancuch")


print(f"Witaj {imie}")
print(f"Twoj wiek to: {wiek}")
print(imie[0] + " " + nazwisko[0])
for i in range (0,5):
    print(lancuch)

lancuch3 = lancuch + lancuch2
print(lancuch3)

lancuch4 = lancuch[:len(lancuch)//2] + lancuch2[:len(lancuch2)//2]
