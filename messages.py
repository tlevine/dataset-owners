#!/usr/bin/env python3
import csv, sys, os, datetime

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout)

# Header
writer.writerow(reader.readrow())

for row in reader:
    dataset, message, *_ = row
    sys.stderr.write(dataset)
    os.system('echo "%s" | xclip')
    input()
    os.system("echo '%s' | xclip" % message)
    notes = input()
    sent = datetime.datetime.now().isoformat()
    newrow = dataset, message, sent, notes
    writer.write(newrow)
