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

<!-- url/paths -->
[1]: https://cran.r-project.org/mirrors.html
[2]: https://youtu.be/NVyOEwOJgNQ