# # Условные операторы и циклы


# import random

# room = 1
# coins = 0
# while room <= 10:
#     print()
#     print('Ты вошел в комнату', room)

#     event = random.randint(1,3)

#     if event == 1:
#         print('На тебя напал монстр👹')
#         print('Ты убежал!😬')
#     elif event == 2:
#         print('🤑 ты нашел 10 монет')
#         coins += 10
#     else:
#         print('🙄 комната пустая!')

#     room +=1

# print()
# print('🧭 Ты прошел все комнаты')
# print(f"👑 ты собрал монет - {coins}")




#Циклы  for, while 
#for - от точки а до точки б и завершается
#while - бесконечный (пока значение не станет ложным!)

# source = 10

# while source != 0:
#     color = str(input('какой свет горит? '))
#     color = color.lower()
#     print(f'кол-во ресурсов - {source}')
#     source -= 1
#     print(f'Остаток ресурсов - {source}')

#     if color == 'зеленый':
#         print('Можете ехать!')

#     elif color == 'желтый':
#         print('Приготовьтесь к движению')

#     elif color == 'красный':
#         print('Стоп!')

#     else:
#         print('Смотрите на знаки!')
#         continue

#     if source == 0:
#         print('Кончились ресурсы требуется кап ремонт!')
#         break





# = - присвоение, == - сравнение или приравнение

# >=, <=, !=, ==, or, and

#с 21 января по 19 февраля.
# day = int(input('Введите день вашего рождения! '))
# month = int(input('Введите месяц вашего! '))

# if day>=21 and day<=31 and month == 1 or day<=19 and day>=1 and month==2:
#     print('Вы Водолей!')
# else:
#     print('Вы не водолей')






# color = str(input('какой свет горит? '))
# color = color.lower()

# if color == 'зеленый':
#     print('Можете ехать!')

# elif color == 'желтый':
#     print('Приготовьтесь к движению')

# elif color == 'красный':
#     print('Стоп!')

# else:
#     print('Смотрите на знаки!')