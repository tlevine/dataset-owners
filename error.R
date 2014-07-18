library(reshape2)

m <- read.csv('data/sent-messages.csv', stringsAsFactors = FALSE)
m$error.sending <- grepl('feedback', m$notes)
m$deleted <- grepl('deleted', m$notes)
m$ok <- m$notes == ''
m$page.load <- grepl('capcha', m$notes, ignore.case = TRUE) | m$notes == "The page doesn't load." | m$notes == "This one doesn't have a contact button."
m$ok[!mapply(any, m$ok, m$deleted, m$error.sending, m$page.load)] <- TRUE

m$status <- factor('', levels = c('ok', 'deleted', 'load.error', 'submit.error'))
m$status[m$ok] <- 'ok'
m$status[m$deleted] <- 'deleted'
m$status[m$page.load] <- 'load.error'
m$status[m$error.sending] <- 'submit.error'
