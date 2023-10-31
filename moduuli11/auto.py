class Auto:
    def __init__(self, input_rekisterinumero, input_huippunopeus, input_kulutus):
        self.rekisterinumero = input_rekisterinumero
        self.huippunopeus = input_huippunopeus
        self.kulutus = input_kulutus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka = self.nopeus * tunnit

    def kulutettu(self):
        return self.kulutus * self.matka / 100

    def jaljella(self):
        return (self.kapasiteetti - super().kulutettu())

    def testi(self):
        print(f'Rekisterinumero: {self.rekisterinumero}, Huippunopeus: {self.huippunopeus}, Kuljettu matka: {self.matka}, Tämän hetken nopeus: {self.nopeus}, kulutus: {self.kulutettu()}')
