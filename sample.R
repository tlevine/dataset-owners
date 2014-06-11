library(sampling)
if (!('owners' %in% ls())) {
  owners <- read.csv('owners.csv', stringsAsFactors = FALSE)
}
N <- nrow(owners)
n <- 32
n.samples <- 4

select <- function() {
  interval <- N/n
  offsets <- sample(1:interval, n.samples, replace = FALSE)
  walls <- cumsum(rep(interval, n)) - interval
  Reduce(function(x,offset){c(x,walls+offset)}, offsets, c())
}

random.dataset <- function(datasets) {
  sample(strsplit(datasets, '\n')[[1]], 1)
}

set.seed(1112)
sample <- owners[select(),]
sample$url <- sapply(sample$datasets, random.dataset, USE.NAMES = FALSE)
paste
