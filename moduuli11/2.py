from sahkoauto import Sahkoauto
from polttomoottoriauto import Polttomoottoriauto

sahkocar = Sahkoauto("ABC-15", 180, 52.5, 20)
moottoricar = Polttomoottoriauto("ACD-123", 165, 32.3, 8)

sahkocar.kiihdyta(80)
sahkocar.kulje(3)
sahkocar.testi()

moottoricar.kiihdyta(80)
moottoricar.kulje(3)
moottoricar.testi()
