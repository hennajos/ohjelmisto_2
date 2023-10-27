class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.sijainti = alin

    def kerros_ylos(self):
        if self.sijainti < self.ylin:
            self.sijainti += 1
        print(f"Hissi on nyt {self.sijainti}. kerroksessa")


    def kerros_alas(self):
        if self.sijainti > self.alin:
            self.sijainti = self.sijainti - 1
        print(f"Hissi on nyt {self.sijainti}. kerroksessa")


    def siirry_kerrokseen(self, haluttu_kerros):
        if self.sijainti < haluttu_kerros:
            while self.sijainti < haluttu_kerros:
                self.kerros_ylos()
        elif self.sijainti > haluttu_kerros:
            while self.sijainti > haluttu_kerros:
                self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissien_lkm):
            hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissi_nro, kohde):
        hissi = self.hissit[hissi_nro - 1]
        hissi.siirry_kerrokseen(kohde)

    def palohalytys(self):
        print(f"Palohälytys! Hissit siirtyvät pohjakerrokseen. ")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.hissit[0].alin)
            break


talo = Talo(1, 12, 2)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 4)
talo.palohalytys()

