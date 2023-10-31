from auto import Auto
class Sahkoauto(Auto):
    def __init__(self, rekisterinumero, huippunopeus, kapasiteetti, kulutus):
        super().__init__(rekisterinumero, huippunopeus, kulutus)
        self.kapasiteetti = kapasiteetti

    def jaljella(self):
        return (self.kapasiteetti - super().kulutettu())

    def testi(self):
        print(f'Rekisterinumero: {self.rekisterinumero}, Huippunopeus: {self.huippunopeus}, Kuljettu matka: {self.matka}, Tämän hetken nopeus: {self.nopeus}, kulutus: {self.kulutettu()} kw, kapasiteetti jäljellä: {self.jaljella()} kw')