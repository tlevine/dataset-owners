library(sampling)
if (!('owners' %in% ls())) {
  owners <- read.csv('owners.csv')
}
N <- nrow(owners)
n <- 32
n.samples <- 16
offsets <- sample(1:(N/n), n.samples, replace = FALSE)
