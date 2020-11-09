mysum = function(x, y=2) {
    z <- x + y
    return(z)
}

ret = mysum(3,5)
print(ret)

ret = mysum(y=10, x=10)
print(ret)

# if we not pass any value for y. y take it default values
mysum = function(x, y=2) {
    z <- x + y
    return(z)
}

ret = mysum(3)
print(ret)

# ret = mysum() # ERROR!!! at least pass an one value for parameter `x`

# Another check
mysum = function(x=1, y, z=5) {
    z <- x + y + z
    return(z)
}

ret = mysum(y=3) # we don't pass mysum(3) something like this
print(ret)


# function return multiple value
myeval = function(x, y) {
    add = x + y
    mul = x * y
    
    result = list('sum'=add, 'mul'=mul)
    return(result)
}

print(myeval(10,2))

# inline function
mysum = function(x, y) x + y
myexp = function(x, y) x ^ y

print(mysum(10, 20))
print(myexp(2,3))
