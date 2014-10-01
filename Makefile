.PHONY: plots

plots: tmp/dataowners.csv
	./bin/plot-dataowners

/tmp/dataowners.csv:
	./bin/log-parser > /tmp/dataowners.csv
