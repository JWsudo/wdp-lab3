ulice = ["Jagodowa", "Lipowa", "Kwiatowa", "Kasztanowa", "Polna"]

for ulica in ulice:
    for i in range(1, 6):
        for j in range(1, 11):
            print(f"{ulica} {i}/{j}")