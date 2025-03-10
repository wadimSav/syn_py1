class Transport:

    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Authobus(Transport):
    def pb(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")
        
bus = Authobus("Renaul Logan", 180, 12)
bus.pb()