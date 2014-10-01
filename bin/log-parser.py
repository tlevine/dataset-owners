import sys
import re
import csv

RESPONSE = re.compile(r'.*/([a-z0-9]{32})/(yes|no).*')

def parse(log):
    writer = csv.writer(sys.stdout)
    writer.writerow(('hash','answer'))
    for row in log:
        m = re.search(RESPONSE, row)
        if m:
            writer.writerow((m.group(1), m.group(2)))

with open('/tmp/access.log') as fp:
    parse(fp)
