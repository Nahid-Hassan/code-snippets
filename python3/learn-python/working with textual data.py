message = 'Hello World'

# print("Hello world")
print(message)

# single quote in text
message = 'Nahid\'s home'  # solve error using escape sequence
print(message)

# or we can solve this problem using double quote ""
message = "Nahid's Home"
print(message)

# work with multiple line
message = """Multiline 
            Quotes"""
print(message)

# print the length of the message
message = 'Hello World'
print(len(message))

# indexing: print the first character of the message
print(message[0])

# print the last character
print(message[len(message) - 1])

# IndexError!!!
# print(message[11]) # string index out of range.

# slicing
# print from index 0  -> upto index 5
print(message[0:5])  # message[:5] same as [0:5]
print(message[6:])  # print from 6 to end of the string

# method
# print message as lowercase
print(message.lower())

# print message as uppercase
print(message.upper())

# print occurrence of a character or string in a string
print(message.count('l'))  # 3
print(message.count('hello'))  # 0 case-sensitive
print(message.count('Hello'))  # 1

# find(str): return the first index where the string start
print(message.find('World'))  # 6
print(message.find('world'))  # -1 : case-sensitive and -1 for no occurrence

# replace(want_to_replace_string, replace_string)
message = message.replace('World', 'Universe')
print(message)

# concatenate
greetings = 'Hello'
name = "Mohammad"

message = greetings + ", " + name
print(message)

message = greetings + ", " + name + ". Welcome!"
print(message)

# using format() -> {} is a placeholder
message = "{}, {}. Welcome!".format(greetings, name)
print(message)


## more advanced f'string'. Can able to pass argument directly into the placeholder
message = f'{greetings}, {name}. Welcome!'
print(message)

# more advanced work: using method inside placeholder
message = f'{greetings}, {name.upper()}. Welcome!'
print(message)

## show all the methods using dir(variable/data_type)
print(dir(message)) # here message is str type that's why it shows all methods of string type 
print(type(message))

## help(class/type)
print(help(str))

## more specifically for example
print(help(str.upper)) # don't use str.upper(). this is perform an execution inside the help function. 