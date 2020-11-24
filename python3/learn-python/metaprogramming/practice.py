class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

    def __len__(self):
        return len(self.name) + 10


person = Person('Mahin', 23)
print(len(person))
