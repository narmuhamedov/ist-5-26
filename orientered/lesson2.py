import lesson1

class ElectrikCar(lesson1.Car):
    def __init__(self, mark, fuel, color, volume, voltage):
        super().__init__(mark, fuel, color, volume)
        self.voltage = voltage

    def __str__(self):
        return super().__str__()+f'\n{self.voltage}'

byd = ElectrikCar(mark='BYD TANK', fuel=False, color='black', volume=0.0, voltage=51.2)
print(byd.traveling('Да'))
print(byd.fuel_consumption())
print(byd)
