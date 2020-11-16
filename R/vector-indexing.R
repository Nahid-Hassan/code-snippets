# Create a vector
x <- c(10, 20, 30, 40, 50, 60)

# In R programming indexing start with 1
x[1] # first element of vector # 10

# R programming support negative indexing
x[-2] # print all the value except index value 2

# slicing 1: 3 => 1, 2, 3
x[1:3] # print first 3 elements

# pass index number
x[c(1,3, 5)]

# calculate length of vector
length(x) # 6

# print NA. when you pass an index which is out of bounds
x[10] # NA

# replace an element
x[-2] = -20
x

x <- c(10, 20, 30, 40, 50, 60)
x[2] = -20
x

x[10] = 100
x # 10 -20  30  40  50  60  NA  NA  NA 100

x <- c(10, 20, 30, 40, 50, 60)
# create vector of element for logical value
y <- c(T, T, F, T, T, F)
x[y]

y <- c(T, F, T) # T, F, T, T, F, T 
x[y]

# print all the value using for loop
for (i in 1 : length(x)) {
    print(x[i])
}

#[1] 10
#[1] 20
#[1] 30
#[1] 40
#[1] 50
#[1] 60

# we can use seq_along(x) # 1,2,3,4,5,6
for (i in seq_along(x)) {
    print(x[i])
}

# or we can use 
for (val in x) {
    print(val)
}
