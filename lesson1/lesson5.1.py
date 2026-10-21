univer=[]
technikum=[]
army=[]
married=[]

abiturients = [
    {'name': 'Igor', 'OPT':110, 'gender': 'male'},
    {'name': 'Aelita', 'OPT':120, 'gender': 'female'},
    {'name': 'Igor', 'OPT':110, 'gender': 'male'},
    {'name': 'Akylai', 'OPT': 40, 'gender': 'female'},
    {'name': 'Ivan', 'OPT':50, 'gender': 'male'},
    {'name': 'Ainazik', 'OPT':30, 'gender': 'female'},
    {'name': 'Ruslan', 'OPT':70, 'gender': 'male'},
    {'name': 'Igor', 'OPT':110, 'gender': 'male'},
    {'name': 'Abbas', 'OPT':80, 'gender': 'male'}
]

def all_abit(lst):
    for i in lst:
        for k,v in i.items():
            print(f'{k}-{v}')
all_abit(lst=abiturients)


def selection(lst, univer:list, technikum:list, army:list,married:list):
    for i in lst:
        if i['OPT'] >=110:
            univer.append(i)
        elif i['OPT'] >=60 and i['OPT']<110:
            technikum.append(i)
        elif i['OPT'] < 60 and i['gender'] == 'male':
            army.append(i)
        elif i['OPT'] < 60 and i['gender'] == 'female':
                    married.append(i)

selection(abiturients, univer, technikum, army, married)
print(f'Универ - {univer}')
print('-'*20)
print(f'Техникум - {technikum}')
print('-'*20)
print(f'Армия - {army}')
print('-'*20)
print(f'Замуж - {married}')
print('-'*20)