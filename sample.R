#!/usr/bin/env Rscript
library(sampling)
library(digest)

if (!('owners' %in% ls())) {
  owners <- read.csv('owners.csv', stringsAsFactors = FALSE)
}

random.dataset <- function(datasets) {
  sample(strsplit(datasets, '\n')[[1]], 1)
}

gethash <- function(salt, userid) {
  digest(paste0(salt, userid), algo = 'md5')
}

message <- function(salt, userid, n.datasets, datasets) {
  hash <- gethash(salt, userid)
  paste0('My name is Thomas Levine, and I have been studying how governments publish data. I am contacting you because you were listed as the "dataset owner" for the following ',
         if(n.datasets > 1) paste(n.datasets, 'datasets') else 'dataset', '.',
         '\n\n', datasets, '\n\n',
         'I would like to know whether you are the person I should contact about this dataset.\n\n',
         'If you are still the contact, please click on the following link.\n',
         'http://dataowners.thomaslevine.com/', hash, '/yes\n\n',
         'If you are no longer the contact or never were the contact, please click on the following link.\n',
         'http://dataowners.thomaslevine.com/', hash, '/no\n\n',
         'And feel free to email me if you have any questions or comments.\n\nThanks')
}

SALT <- Sys.getenv('SALT')

owners <- owners[order(owners$n.datasets),] # Order by number of datasets so that the sampling works.

n <- 256

# Do the systematic sampling, weighted by the number of datasets.
set.seed(1112)
s <- UPsystematic(inclusionprobabilities(owners$n.datasets,n))

sample <- owners[s == 1,]
sample$url <- sapply(sample$datasets, random.dataset, USE.NAMES = FALSE) # Select one dataset URL per dataset
messages <- data.frame(
  dataset = sample$url,
  message = mapply(message, SALT, sample$owner, sample$n.datasets, sample$datasets, USE.NAMES = FALSE)
)
messages$sent <- ''
messages$notes <- ''

for.analysis <- data.frame(
  owner.id = sample$owner,
  owner.hash = mapply(gethash, SALT, sample$owner),
  n.datasets = sample$n.datasets
)
write.csv(messages, file = 'data/messages.csv', row.names = FALSE)
write.csv(for.analysis, file = 'data/for-analysis.csv', row.names = FALSE)
