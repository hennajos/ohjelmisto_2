from auto import Auto
car = Auto('ABC-123', 142)
car.testi()

print(f'Rekisterinumero: {car.rekisterinumero}, Huippunopeus: {car.huippunopeus}, Matka: {car.matka}, Nopeus: {car.nopeus}')

car.kiihdyta(30)
car.kiihdyta(70)
car.kiihdyta(50)
car.testi()
print(f"Auton nopeus kiihdytyksen jälkeen {car.nopeus}")

car.kiihdyta(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen {car.nopeus}")

