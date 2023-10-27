import random
from auto import Auto
import prettytable
from prettytable import PrettyTable

class Auto:
    def __init__(self, input_rekisterinumero, input_huippunopeus):
        self.rekisterinumero = input_rekisterinumero
        self.huippunopeus = input_huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        uusinopeus = self.nopeus + muutos
        if uusinopeus < 0:
            self.nopeus = 0
        elif uusinopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = uusinopeus

    def kulje(self):
        self.matka += self.nopeus

autot = []

for i in range(1, 11):
    rekisterinumero = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisterinumero, huippunopeus)
    autot.append(auto)


while True:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje()


    if any(auto.matka >= 10000 for auto in autot):
        break

taulukko = PrettyTable()
taulukko.field_names = ["Rekisteritunnus", "Huippunopeus (km/h)", "Matka (km)", "Nopeus (km/h)"]

for auto in autot:
    taulukko.add_row([auto.rekisterinumero, auto.huippunopeus, auto.nopeus, auto.matka])

print(taulukko)


