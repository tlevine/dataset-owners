library(sampling)
if (!('owners' %in% ls())) {
  owners <- read.csv('owners.csv')
}
N <- nrow(owners)
n <- 32
interval <- N/n
n.samples <- 4

set.seed(1112)
offsets <- sample(1:interval, n.samples, replace = FALSE)

walls <- cumsum(rep(interval, n)) - interval

sample <- Reduce(function(x,offset){c(x,walls+offset)}, offsets, c())
