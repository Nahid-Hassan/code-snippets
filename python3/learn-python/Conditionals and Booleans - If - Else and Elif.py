if True:
    print('Condition was True')

language = 'Python3'

if language == 'Python3':
    print('Yes language is Python3')

# Comparison Operators

# Equal               :  3  == 2  ==> False
# Not Equal           :  3  != 2  ==> True
# Greater Than        :  3  >  2  ==> True
# Less Than           :  3  <  2  ==> False
# Greater or Equal    :  3  >= 2  ==> True
# Less or Equal       :  3  <= 2  ==> False
# object identity     :  is

'''
Definition and Usage
The is keyword is used to test if two variables refer to the same object.

The test returns True if the two objects are the same object.

The test returns False if they are not the same object, even if the two objects are 100% equal.

Use the == operator to test if two variables are equal.
'''

language = 'Java'

if language == 'Python3':
    print('Yes language is Python3')
elif language == 'Java':
    print('Yes language is Java')
elif language == 'JavaScript':
    print('Yes language is JavaScript')
else:
    print('No Match')

# and
# or
# not -> switch a boolean

user = 'Admin'
logged_in = False

# and
if user == 'Admin' and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# or
if user == 'Admin' or logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

# not
if not logged_in:
    print("Please Logged in")
else:
    print("Welcome")

# is
# if id(object) of both object is same then return True else False

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

print(id(a))  # 140136814353088
print(id(b))  # 140136805134784

a = b

print(id(a))  # 140136805134784
print(id(b))  # 140136805134784

print(a is b)

'''
# False Values
    # False
    # None
    # Zero of any numeric value
    # Any empty sequence. For Example: (), [], ''.
    # Any empty mapping. For Example:  {}
'''
condition = False

if condition:
    print("Evaluate to True")
else:
    print("Evaluate to False")

false_values = [False, True, None, 0, 1, tuple(), list(), '', ' ', dict()]
print(false_values)

for values in false_values:
    condition = values

    if condition:
        print(f"{condition}, Evaluate to True")
    else:
        print(f"{condition}, Evaluate to False")
