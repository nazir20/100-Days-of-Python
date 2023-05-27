# Python Object oriented Programming

class Employee:
    # class variables
    raise_amount = 1.04
    num_of_employees = 0

    # constructor
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        Employee.num_of_employees += 1

    @property
    def email(self):
        return '{}.{}@company.tr'.format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        print('Delete Full Name!')
        self.first_name = None
        self.last_name = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    # class variables
    raise_amount = 1.06

    # constructor
    def __init__(self, first_name, last_name, pay):
        super().__init__(first_name, last_name, pay)
        self.programming_langs = []

    def add_programming_lang(self, programming_langs):
        langs = programming_langs.split('-')
        for pl in langs:
            self.programming_langs.append(pl)

    def developer_info(self):
        print(f'Full Name: {self.full_name}')
        print(f'Salary: {self.pay}')
        print('Programming Languages', end=': ')
        for lang in self.programming_langs:
            print(lang, end=' ')


class Manager(Employee):

    # constructor
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp_info(self):
        for emp in self.employees:
            if isinstance(emp, Developer):
                Developer.developer_info(emp)
            else:
                print(f'Full Name: {emp.full_name}')
                print('Type: None')

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return '{}-{}'.format(self.full_name, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name)
# emp_str_1 = 'John-Doe-8500'
# emp_str_2 = 'Demir-Egemen-9000'
#
# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_2 = Employee.from_string(emp_str_2)
# print(new_emp_1.full_name())
# import datetime
#
# my_date = datetime.date(2023, 5, 27)
# print(Employee.is_workday(my_date))
#
# dev1 = Developer('Ali', 'Aka', 9500)
# dev1.add_programming_lang('JavaScript-PHP-Python')
# # dev1.developer_info()
# mng1 = Manager('Nazir', 'Sharifi', 12000)
# # mng1.add_employee(dev1)
# # mng1.print_emp_info()
# print(mng1)

# emp1 = Manager('Ege', 'Aka', 12000)
# emp2 = Manager('Muge', 'Deniz', 15000)
# print(emp1+emp2)
#
# print(len(emp1))
# del emp1.full_name
