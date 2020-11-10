# typeof(..) return atomic types of the variable

x <- 10
typeof(x) # integer

x <- 10.5
typeof(x) # double

x <- T
typeof(x) # logical

x <- 'Mahin'
typeof(x) # character

# create a vector in R

# using c(....)
x <- c(10,20,20)
x
typeof(x)

# using assign
assign('y', c(20, 23.4, 2))
typeof(y)

assign('t', c('a', 10, 39, 2.4))
typeof(t)

# using sequence of number
y <- 1:6
typeof(y)
y

z <- seq(3, 6)
z
typeof(z)

w = c(y, z)
w

### multiple assign
x <- y <- z <- c(seq(1,6))
x
y
z

#### using `vector` 
### vector(mode, length=integer) # default 0, FALSE, empty string

x <- vector('numeric', length = 4)
x

x <- vector('logical', length = 4)
x

x <- vector('character', length = 4)
x

x <- vector('double', length = 4)
x


## length()
length(x)

### In R programming language indexing starting from 1. Not Zero
