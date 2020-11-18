# basic function
# def func_name(parameter):
#     # write your code here
#     return something or not
#     if not return anything by default return None

# # function call
# func_name(1)

def hello_func():
    print('Hello Function')


hello_func()
print(hello_func())
print(hello_func)

'''
# basic function...
Hello Function
Hello Function
None
<function hello_func at 0x7f3b98a57e50>
'''


# function with return something
def return_func():
    return 'return hello'


print(return_func())
print(return_func().upper())  # chain call

### pass arguments ####


def welcome(greeting, name='You'):
    return f'{greeting}, {name} Function.'


message = welcome('Welcome')
print(message)
print(welcome('Hi'))

# or

message = welcome('Welcome', "Mahin")
print(message)
print(welcome('Hi', 'Meem'))


##### args and kwargs ########
def student_info(*args, **kwargs):
    print(args)  # tuple
    print(kwargs)  # dict


student_info('Math', 'Art', name='J. Smith', age=23)
'''
('Math', 'Art')
{'name': 'J. Smith', 'age': 23}
'''

courses = ['Matt', 'Art']
info = {'name': 'J. Smith', 'age': 23}

student_info(courses, info)
'''
(['Matt', 'Art'], {'name': 'J. Smith', 'age': 23})
{}
'''
# * and ** unpack the actual values and pass them individually. 
student_info(*courses, **info)
'''
('Matt', 'Art')
{'name': 'J. Smith', 'age': 23}
'''
