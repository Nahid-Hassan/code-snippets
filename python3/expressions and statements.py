# sort a nested dict
users = [{"first_name":"Helen", "age": 39},
		 {"first_name":"Buck", "age":10},
		 {"first_name":"anni", "age":9}
		]

users = sorted(users, key=lambda user: user["first_name"].lower())
print(users)

"""what is the problem with this code? it's not easy to understand this code
This code fails to address issues such as missing keys or if the dictionary 
is correct or not. Let's rewrite this code using a function and try to code 
make more readable and correct."""

def get_user_name(users):
	"""Get name of the user in lowercase"""
	return users['first_name'].lower()

def get_sorted_dictionary(users):
	"""Sort the nested dictionary"""
	if not isinstance(users, dict):
		raise ValueError("Not a correct dictionary")
	if not len(users):
		raise ValueError("Empty dictionary")
	
	users_by_name = sorted(users, key=get_user_name)
	return users_by_name
