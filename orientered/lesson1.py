class Car:
    def __init__(self, mark, fuel, color, volume):
        self.mark = mark
        self.fuel = fuel
        self.color = color
        self.volume = volume

    def traveling(self, yes_no):
        return f'Эта машина {self.mark} может путешевствовать {yes_no}'

    def fuel_consumption(self):
        if self.volume >= 3.0:
            return f'{self.mark} - не экномная'
        elif self.volume <=1.8:
            return f'{self.mark}-экономичная'

    

    def __str__(self):
        return f'{self.mark}\n{self.fuel}\n{self.color}\n{self.volume}'
    

lexus = Car(mark='lexus Rx 300', fuel='АИ-92', color='Черный', volume=3.0)
print(lexus)
print('--------------')
mazda = Car(mark='mazda 6', fuel='AИ-95', color='Красный', volume=1.8)
print(mazda)

print(lexus.traveling('Да'))
print(mazda.traveling('Нет'))

print(lexus.fuel_consumption())
print(mazda.fuel_consumption())