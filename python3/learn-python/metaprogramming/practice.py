# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f'{self.name} is {self.age} years old.'

#     def __len__(self):
#         return len(self.name) + 10


# person = Person('Mahin', 23)
# print(len(person))

class Test:

    """ cls: class Test itself. Not object of class Test. It class itself """
    def __new__(cls, x):
        print(f'__new__, cls={cls}')
        return super().__new__(cls)

    def __init__(self, x):
        print(f'__init__, self={self}')
        self.x = x

    def __repr__(self):
        return f'name is name'

test = Test(2)
