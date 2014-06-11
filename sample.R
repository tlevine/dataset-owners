library(sampling)
owners <- read.csv('owners.csv')
N <- nrow(owners)
n <- 60
n.samples <- 5
offsets <- floor(runif(n.samples, 1, N/n)))
