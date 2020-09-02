# Variables and Functions

# Variable names
names = "Python"
job_title = "Software Engineer"
populated_countries_list = []

# Nonmangling names
_books = {} # variable name to define private
__dict = [] # prevent name mangling with python in-build lib

"""You should use one underscore(_) as a prefix for the internal variable
of a class, where you don't want an outside class to access the variable.
This is just a convention; Python doesn't make a variable with a single 
underscore prefix private."""

# Normal function names
# function name with single underscore
def get_data():
	# write you code here
	pass

def calculate_tax_data():
	# write your code here
	pass

"""The same rules apply to private methods and methods where you want to
prevent name mangling with built-in python functions."""
# private method with single underscore
def _get_data():
	# write your code here
	pass

# double underscore to prevent name mangling with other in-build functions
def __path():
	# write your code here
	pass


# function names 
# wrong way
def get_user_info(id):
	db = get_db_connection()
	user = execute_query_for_user(id)
	return user

# Right way
def get_user_by(user_id):
	db = get_db_connection()
	user = execute_query_for_user(user_id)
	return user

# Classes
"""The names of classes should be in camel case like in most other languages"""
class UserInformation:
	def get_user(id):
		db = get_db_connection()
		user = execute_query_for_user()
		return user


# Constants names
TOTAL = 56
TIMOUT = 6
MAX_OVERFLOW = 7

# function and method arguments
"""Function and method arguments should follow the same rules as variables and
methods names. A class method has self as the first keyword argument compared to
functions that don't pass self as a first keyword parameter."""

def calculate_tax(amount, yearly_tax):
	pass

class Player:
	def get_total_score(self, player_name):
		pass
