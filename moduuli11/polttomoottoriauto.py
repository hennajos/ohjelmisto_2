from auto import Auto
class Polttomoottoriauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, bensatankki, kulutus):
        super().__init__(rekisterinumero, huippunopeus, kulutus)
        self.bensatankki = bensatankki

    def jaljella(self):
        return (self.bensatankki - super().kulutettu())

    def testi(self):
        print(f'Rekisterinumero: {self.rekisterinumero}, Huippunopeus: {self.huippunopeus}, Kuljettu matka: {self.matka}, Tämän hetken nopeus: {self.nopeus}, kulutus: {self.kulutettu()} l, kapasiteetti jäljellä: {self.jaljella()} l')