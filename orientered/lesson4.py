class Dog:
    def __init__(self, name='Аргоша'):
        self.name = name

    def make_sound(self):
        return f'{self.name} Гав-Гав'


class Cat:
    def __init__(self, name='Гарик'):
        self.name = name

    def make_sound(self):
        return f'{self.name} Мяу-Мяу'


class Cow:
    def __init__(self, name='Милка'):
        self.name = name

    def make_sound(self):
        return f'{self.name} Му-му'


def sound_animal(animal_obj):
    print(f'Животное {animal_obj.name} - {animal_obj.make_sound()}')


dog = Dog()
cat = Cat()
cow = Cow()
# или с именами: dog = Dog('Шарик')

sound_animal(animal_obj=dog)
sound_animal(animal_obj=cat)
sound_animal(animal_obj=cow)





# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print('Сумма пополнения должна быть больше 0')

# account = BankAccount('Иван', 1000)
# account.deposit(500)
# print(account.get_balance())
# try:
#     print(account.__balance)
# except:
#     print('системная ошибка сервера 502')