class Transport:

    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"


class Authobus(Transport):
    def pb(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")
        
    def seating_capacity(self, capacity = 50):
       return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"
        
bus = Authobus("Renaul Logan", 180, 12)
print(bus.seating_capacity())