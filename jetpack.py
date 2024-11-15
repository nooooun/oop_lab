from backpack import Backpack

class Jetpack(Backpack):
    def __init__(self, name, colour, max_size = 2, fuel = 10):
        super().__init__(name, colour, max_size)
        self.fuel = fuel

    def __str__(self):
        return f"{self.name}'s jetpack coloured {self.colour} contains {self.contents} and has {self.fuel} liters of fuel."

    def dump(self):
        super().dump()
        self.fuel = 0

    def fly(self, amount_of_fuel):
        if amount_of_fuel > self.fuel:
            print("Not enough fuel!")
            return
        self.fuel -= amount_of_fuel