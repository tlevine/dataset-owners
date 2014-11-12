.PHONY: plots

plots: /tmp/dataowners.csv
	./bin/plot-owners
	./bin/plot-errors

/tmp/dataowners.csv:
	./bin/log-parser > /tmp/dataowners.csv
