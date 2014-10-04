.PHONY: plots

plots: /tmp/dataowners.csv
	./bin/plot-owners

/tmp/dataowners.csv:
	./bin/log-parser > /tmp/dataowners.csv
