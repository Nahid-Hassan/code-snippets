x <- 10
x
# To know variable data types 
class(x)


# Create integer variable using as.interger() method
y <- as.integer(10) 
print(y)
class(y)
is.integer(y)

# Pass floating point number
y <- as.integer(10.35) 
print(y)
class(y)
is.integer(y)

# Create integer variable using `L`
y <- 105L 
print(y)
class(y)
is.integer(y)

# We can also pass string-> numeric value as input
y <- as.integer('10.35') # it works because `10.35` is numeric value
print(y)
class(y)
is.integer(y)

# But if we pass string -> ex. name as input
y <- as.integer('Jhon')
print(y)
class(y)
is.integer(y)


x <- 4 + 3i # complex
x <- T      # logical T: TRUE
x <- F      # logical F: FALSE
x <- "Jack" # character
x <- as.character(3.75) # convert numerical to character
is.character(x) # TRUE
