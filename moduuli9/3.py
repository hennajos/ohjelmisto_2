from auto import Auto
car = Auto('ABC-123', 142)

car.kiihdyta(30)
car.kiihdyta(70)
car.kiihdyta(50)
car.testi()

car.kiihdyta(-200)
car.kiihdyta(30)
car.kulje(1)
car.testi()

car.kulje(2)
car.testi()