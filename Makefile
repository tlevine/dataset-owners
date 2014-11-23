.PHONY: plots

plots: /tmp/dataowners.csv
	./bin/plot-owners
	./bin/plot-errors

/tmp/dataowners.csv:
	./bin/log-parser > /tmp/dataowners.csv
	sed '1 d' data/email-responses-hash.csv >> /tmp/dataowners.csv
