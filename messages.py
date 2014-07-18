#!/usr/bin/env python3
import csv, sys, os, datetime

reader = csv.reader(open('data/messages.csv','r'))
out = open('data/sent-messages.csv','w')
writer = csv.writer(out)

# Header
writer.writerow(next(reader))

def write(info):
    sys.stderr.write(info + '\n')
    os.system("echo '%s' | xclip" % info)

for row in reader:
    try:
        dataset, message, sent, _ = row
    except:
        sys.stderr.write(str(row))
        raise
    if sent == '':
        write(dataset)
        input()
        write(message)
        notes = input()
        sent = datetime.datetime.now().isoformat()
        newrow = dataset, message, sent, notes
        writer.writerow(newrow)
        out.flush()
