# The R Project for Statistical Computing

[Tutorial link][2]

## Getting Started

R is a free software environment for statistical computing and graphics. It compiles and runs on a wide variety of UNIX platforms, Windows and MacOS. To `download R`, please choose your preferred [CRAN][1] mirror.

If you have questions about R like how to download and install the software, or what the license terms are, please read our answers to frequently asked questions before you send an email.

### First R Program

```r
print('Hello R Program')
```

```r
> print('Hello R Program')
[1] "Hello R Program"
```

```sh
$ Rscript test.R
[1] "hello world"
$ R CMD BATCH test.R
$ ls
test.R  test.Rout
```

### Basic Mathematical Operators

```r
x <- 10 # assign 10 into variable x
y <- 20 # assign 20 into variable y

z <- x +  y # add x and y and assign result in variable z
print(z) # show the value of variable z
```

![Arithmetic Operator](./images/math-expression.png)

```r
> 10 - 5
[1] 5

> 10 * 5
[1] 50

> 10 / 3
[1] 3.333333

> 10.4 / 3
[1] 3.466667

> 10 / 2
[1] 5

> 10.0 / 2
[1] 5

> 10 ** 3
[1] 1000

> 10 ^ 3
[1] 1000

> 9 ** .5
[1] 3

> 9 ** 1 / 2   # Because ** > / (precidence)
[1] 4.5

> 9 ** (1 / 2)
3
```

![Special Operator](./images/special-expression.png)

```r
> 14 %% 3
[1] 2

> 14.5 %% 3
[1] 2.5

> 14 %% 3.4
[1] 0.4
```

### Integer Division

Integer division always return the floor value

```r
> 8 / 3
[1] 2.666667

> 8 %/% 3
[1] 2

> - 8 / 3
[1] -2.666667

> -8 %/% 3
[1] -3
```

#### Note: we cannot add `string and integer` numbers and also `string and string`

### Variables

![variable-1](images/variable-1.png)

![variable-2](images/variable-2.png)

![variable-3](images/variable-3.png)

### R is Dynamically Type Language

![variable-4](images/variable-4.png)

![variable-5](images/variable-5.png)

#### Declare Variable

```r
age <- 10
marks1 <- 20
subject_name <- 'R'

# cannot use
# $subject_name <- 'Java'
# 3name <- 'Alex'
```

#### Variable Properties

```sh
age <- 10
typeof(age) # double
mode(age) # numeric
storage.mode(age) # double
class(age) # numeric

subject_name = 'R'
typeof(subject_name) # character
mode(subject_name) # character
storage.mode(subject_name) # character
class(subject_name) # character

> marks1 <- 20.10
> typeof(marks1)
[1] "double"
> mode(marks1)
[1] "numeric"
> storage.mode(marks1)
[1] "double"
> class(marks1)
[1] "numeric"

> flag = TRUE
> typeof(flag)
[1] "logical"
> mode(flag)
[1] "logical"
> storage.mode(flag)
[1] "logical"
> class(flag)
[1] "logical"
```

### Variable Expression

```r
x <- 10
y <- 20
sum = x + y # expression
```

<!-- url/paths -->
[1]: https://cran.r-project.org/mirrors.html
[2]: https://youtu.be/NVyOEwOJgNQ
