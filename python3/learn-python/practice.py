from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    city: str
    age: int
    is_senior: bool = field(init=False)

    def __post_init__(self):
        if self.age >= 60:
            self.is_senior = True
        else:
            self.is_senior = False


p = Person('Mahin', 'Jamalpur', 69)
print(p.is_senior)

@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b

print('work')
c = C(10, 20)
print(c)
