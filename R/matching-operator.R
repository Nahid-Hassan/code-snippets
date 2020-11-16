# matching operator: %in%

x <- c(10,20,30,40,50,60)

10 %in% x # TRUE

y <- 20

y %in% x # TRUE

y <- c(10, 20, 24, 30)

y %in% x # TRUE, TRUE, FALSE, TRUE
