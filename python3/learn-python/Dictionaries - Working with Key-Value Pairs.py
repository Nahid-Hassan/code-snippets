################# Dict #######################
#### dict are mutable #################

student = {'name': 'Smith', 'age': 24, 'courses': ['art', 'bangla', 'english']}

print(student)
# {'name': 'Smith', 'age': 24, 'courses': ['art', 'bangla', 'english']}
print(student['courses'])
# ['art', 'bangla', 'english']

# pass wrong key raise an error: KeyError

# to overcome this using get() method
# get('wrong_key'): return None
print(student.get('name'))  # Smith
print(student.get('phone'))  # None

# we can also pass if key is not found which text show in the console
print(student.get('phone', 'Not Found'))

student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))
student['phone'] = '555-ds55'
print(student.get('phone', 'Not Found'))

student.update({'name': 'J. Smith', 'age': 24,
                'courses': ['art', 'bangla', 'english']})

print(student)

age = student.pop('age')
print(age)

## keys(), values()
print(student.keys())
print(student.values())

# items() : returns (keys,values)
print(student.items())

for key, values in student.items():
    print(key, values)