########### List #################

courses = ['Physics', 'Mathematics', "Computer Science", 'History']

print(courses)

# len() : return how many elements in the list
print(len(courses))  # currently 4

#### List Indexing ########
print(courses[0])
print(courses[:3])
print(courses[2:4])

print(courses[-1])  # return last item


# append(object)
courses.append('Art')
print(courses)

## insert(index_position, object)
courses.insert(0, 'Art')
print(courses)

courses.insert(0, 'Bangla')
print(courses)

# insert a list into list
course_2 = ['Business', 'IBA']
courses.insert(0, course_2)
print(courses)

print(courses[0])  # ['Business', 'IBA']

# to overcome list inside a list we can use extend
course_2 = ['Business', 'IBA']
courses.extend(course_2)
print(courses)

# remove ['Business', 'IBA'] this portion
# remove(object)

courses.remove(course_2)
print(courses)

# pop() : remove and return last element from the list
last_course = courses.pop()
print(courses)
print(last_course)  # IBA

# revese() : reverse the list
courses.reverse()
print(courses)

# sort() : sort list  in assending order by default
courses.sort()  # base upon lexicographical order
print(courses)

nums = [3, 5, 3, 23, 22, 23]
print(nums)
nums.sort()
print(nums)

# sort(reverse=True/False)
#  True ---> Assending: default
#  False --> Desending: not default
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

# here we see sort() altered the original list
# in case of this situation we can use
# sorted(object) : return sorted list

sorted_courses = sorted(courses)
print(sorted_courses)

## min(), max(), sum()
print(nums)       # [23, 23, 22, 5, 3, 3]
print(min(nums))  # 3
print(max(nums))  # 23
print(sum(nums))  # 79

# index() : return the index of the element. if not found return ValueError
print(courses)
print(courses.index('Mathematics'))  # 1
print(courses.index('Urdu'))  # ValueError: 'Urdu' is not in  list

## in ##
print('Art' in courses)  # True
print('Math' in courses)  # False

for course in courses:
    print(course)

# enumerate(): return index and elements
for index, course in enumerate(courses):
    print(index, course)

# enumerate(object, start=int_value): return index and elements
for index, course in enumerate(courses, start=1):
    print(index, course)

# join method in string
course_str = ', '.join(courses)
print(course_str)

# split(object, sep)
# print(help(str.split))
'''

split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.
'''
new_list = course_str.split(',')
print(new_list)

################# Tuples #################
####### We cannot modify tuple #############
####### tuple are immutable #############


######################## first understand mutable and immutable ##################

####### first mutable #######
list_1 = ['history', 'math', 'art']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'CSE'

print(list_1)
print(list_2)

'''
## Output:
['history', 'math', 'art']
['history', 'math', 'art']
['CSE', 'math', 'art']
['CSE', 'math', 'art']
'''

####### second immutable #######
tuple_1 = ('history', 'math', 'art')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'CSE'  # Error!! didnot support

# print(tuple_1)
# print(tuple_2)

# count()
print(tuple_1.count('math'))

# index()
print(tuple_1.index('art'))
# print(tuple_1.index('not found')) ### ValueError: tuple.index(x): x not in tuple

##################### Set #########################
### we cannot add duplicate value in set ######
cs_courses = {'art', 'bangla', 'english', 'math', 'art'}
print(cs_courses)

# in : work first rather than list and tuple
print('art' in cs_courses)

### we can also perform set operation ##########
cs_courses = {'C', 'C++', 'english', 'math', 'design'}
art_courses = {'design', 'english', 'fine'}
print(cs_courses)
print(art_courses)

# intersection()
print(cs_courses.intersection(art_courses))
# difference()
print(cs_courses.difference(art_courses))
# union
print(cs_courses.union(art_courses))

# create empty list, tuple, and set

empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {}  # error!!! not a right way. {} -> create dictionary
empty_set = set()
