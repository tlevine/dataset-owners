#!/usr/bin/env python3
import csv, sys, os, datetime

reader = csv.reader(open('data/messages.csv','r'))
sent_so_far = set(row[0] for row in csv.reader(open('data/sent-messages.csv')) if row[2] != '') if os.path.isfile('data/sent-messages.csv') else set()

wasfile = os.path.isfile('data/sent-messages.csv')
out = open('data/sent-messages.csv','a')
writer = csv.writer(out)

# Header
if not wasfile:
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
    if dataset not in sent_so_far:
        write(dataset)
        input()
        write(message)
        notes = input()
        sent = datetime.datetime.now().isoformat()
        newrow = dataset, message, sent, notes
        writer.writerow(newrow)
        out.flush()
