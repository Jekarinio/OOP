class Student:
    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.groupNumber = group_number

    def get_name(self):
        return f'Имя студента - {self.name}'

    def get_age(self):
        return f'возраст студента - {self.age}'

    def get_group_number(self):
        return f'группа студента - {self.groupNumber}.'


Petya = Student("Петя", 18, "10B")
print(f'{Petya.get_name()}, {Petya.get_age()}, {Petya.get_group_number()}')



