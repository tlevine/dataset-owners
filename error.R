m <- read.csv('data/sent-messages.csv', stringsAsFactors = FALSE)
m$error.sending <- grepl('feedback', m$notes)
m$deleted <- grepl('deleted', m$notes)
m$ok <- m$notes == ''
m$page.load <- grepl('capcha', m$notes, ignore.case = TRUE) | m$notes == "The page doesn't load." | m$notes == "This one doesn't have a contact button."
m$ok[!mapply(any, m$ok, m$deleted, m$error.sending, m$page.load)] <- TRUE

