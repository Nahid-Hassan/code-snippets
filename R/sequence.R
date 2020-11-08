x = 1: 10
x
y = 10: 1
y

x = 1 : 10 * 10 # first create the sequence then multiply with 10
x

x = 1: 10 - 1 # first create the sequence then subtract by 1
x

x = 5 # assign x to 5
1: x # show 1 to 5 in the console
1 : x - 1
1 : (x - 1)

# create a sequence using seq(start_point, end_point)
x <- seq(1, 5)
x

x = seq(10) # by default begin from 1
x # 1.........10

x = seq(from=5, to=2)
print(x)
x = seq(from=1, to =5)
print(x)

x = seq(from=5, to=50, by=5)
print(x)

# or

x = seq(5, 50, 5)
print(x)

# length argument
x = seq(5, 100, lenght=10)
x

x = seq(1.0, 2.0, 0.1)
x

# by or third argument cannot be zero.
# !!!ERROR!!!
# x = seq(1, 5, 0) # occur an error

