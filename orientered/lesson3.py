class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f'Имя: {self.name}-Оклад: {self.salary} сом'

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.prog_lang = programming_language


company_employees = [
    Manager(name='Alex A.', salary=12000, team_size=5),
    Developer(name='Dmitrii B.', salary=5000, programming_language='QBasic'),
    Developer(name='Rustik R.', salary=50000, programming_language='Python'),
    Manager(name='Asena A.', salary=30000, team_size=10),
    Developer(name='Igor I.', salary=90000, programming_language='Java'),
    Developer(name='Marat M.', salary=90000, programming_language='Java'),
    Manager(name='Gulina G.', salary=15000, team_size=20),
    Developer(name='Segrei S.', salary=10000, programming_language='Python')
]
print('---Список всех сотрудников---')
for emp in company_employees:
    print(emp.get_details())

    if isinstance(emp, Manager):
        if emp.team_size >=10:
            bonus = 15000
        else:
            bonus = 3000
        print(f'Менеджер {emp.name} получает бонус {bonus} за управления командой')

    elif isinstance(emp, Developer):
        if emp.prog_lang == "Java" or emp.prog_lang == "Python":
            bonus = 12000
            print(f'Разработчик {emp.name} получает бонус {bonus} за использование языка {emp.prog_lang}')
        else:
            bonus = 1000
            print(f'Разработчик {emp.name} получает бонус {bonus} за использование языка {emp.prog_lang} ')

    final_salary = emp.salary + bonus

    print(f'Итоговая выплата {emp.name}: {final_salary}сом\n')