#!/usr/bin/env python3
import csv, sys, os, datetime

reader = csv.reader(open('data/messages.csv','r'))
sent_so_far = set(row[3] != '' for row in csv.reader(open('data/sent-messages.csv'))) if os.path.isfile('data/sent-messages.csv' else set()

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
    if sent not in sent_so_far:
        write(dataset)
        input()
        write(message)
        notes = input()
        sent = datetime.datetime.now().isoformat()
        newrow = dataset, message, sent, notes
        writer.writerow(newrow)
        out.flush()
