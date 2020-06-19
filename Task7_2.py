from abc import ABC, abstractmethod

class Fabric(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def get_S_a(self):
        return self.width / 6.5 + 0.5

    @abstractmethod
    def get_S_b(self):
        return self.height * 2 + 0.3

class Topcoat(Fabric):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.S_a = round(self.width / 6.5 + 0.5)

    def get_S_a(self):
        super().S_a()

    def get_S_b(self):
        super().S_b()

    def __str__(self):
        return f'Кол-во ткани для пальто: {self.S_a} m^2'


class Suit(Fabric):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.S_b = round(self.height * 2 + 0.3)

    def get_S_a(self):
        super().S_a()

    def get_S_b(self):
        super().S_b()

    def __str__(self):
        return f'Кол-во ткани для костюма: {self.S_b} m^2'

topcoat = Topcoat(21, 5)
suit = Suit(3, 7)
print(topcoat)
print(suit)

class Fabric:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def get_S_all(self):
        return str(f'Общая площадь всей ткани: \n'
                   f' {(self.width // 6.5 + 0.5) + (self.height * 2 + 0.3)}' 'm^2')


f = Fabric(21, 7)
print(f.get_S_all)