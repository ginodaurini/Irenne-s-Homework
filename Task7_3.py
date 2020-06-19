class Cellule:
    def __init__(self, quota):
        self.quota = int(quota)

    def __str__(self):
        return f'Result_str: {self.quota * "*"}'

    def __add__(self, other):
        return Cellule(self.quota + other.quota)

    def __sub__(self, other):
        return self.quota - other.quota if (self.quota - other.quota) > 0 else print('None!')

    def __mul__(self, other):
        return Cellule(int(self.quota * other.quota))

    def __truediv__(self, other):
        return Cellule(round(self.quota // other.quota))


    def make_order(self, cellules_in_row):
        row = ''
        for i in range(int(self.quota / cellules_in_row)):
            row += f'{"*" * cellules_in_row} \\n'
        row += f'{"*" * (self.quota % cellules_in_row)}'
        return row

cellules1 = Cellule(13)
cellules2 = Cellule(3)
print(cellules1)
print(cellules1 + cellules2)
print(cellules2 - cellules1)
print(cellules2.make_order(3))
print(cellules1.make_order(9))
print(cellules1 / cellules2)