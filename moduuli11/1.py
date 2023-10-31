class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"{self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.kirjoittaja}, {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)
    def tulosta_tiedot(self):
        print(f"{self.nimi}, {self.paatoimittaja}")

kirja = Kirja("Hytti no 6", "Rosa Liksom", "200")
kirja.tulosta_tiedot()
lehti = Lehti("Aku Ankka", "Aki Hyyppä")
lehti.tulosta_tiedot()