#Списки, кортежи, словари


student = {
    'name': 'Ivanov Ivan',
    'age': 24,
    True: 'education',
    False: 123,
    'numbers': ['0550123321', '077012321']
}

student['numbers'].append('234')


#add
student['city'] = 'Bishkek'
student.update(car=False)

#delete
del student[False]

#update
student['age']=25
student.update(age=30)


print(student['numbers'])
print(student)

for k,v in student.items():
    print(f'{k}-{v}')



# data_type = (3.14, 5,1,4, 'm', 'a','d', True)

# letters = []
# numbers = []

# for i in data_type:
#     if type(i) == str:
#         letters.append(i)
#     else:
#         numbers.append(i)

# letters.append('A')
# letters.reverse()

# numbers.remove(3.14)

# letters.append(numbers.pop(-1))

# numbers.append(2)
# numbers.append(3)

# numbers.sort()

# letters = tuple(letters)
# numbers = tuple(numbers)

# print(letters)
# print('-'*5)
# print(numbers)




# names = ('Naruto', 'Saskey', 'Sakura')
# names = list(names)
# names.append('Hinata')
# names = tuple(names)

# print(names)




# data_type_1 = [1,2,3,4,5,6,7]
# data_type_2 = ['J.Sean', 'FloRida', '50 Cent', 'Kesha']

# data_type_2.append(data_type_1.pop(4))


#Расширение списка другим списком
#data_type_1.extend(data_type_2)

# print(data_type_2)







# data_types = ['Ivanov', 23, True, 33.44, False, 33, 'Ivan']

# #add
# data_types.append('Radomir')
# #add 2
# data_types.insert(0, 'Iphone')
# #delete
# data_types.remove(23)
# del data_types[0]
# data_types[-2] = 'Dean W.'


#print(data_types)