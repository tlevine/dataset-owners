#!/usr/bin/env python3
import csv, sys, os, datetime

reader = csv.reader(open('messages.csv','r'))
writer = csv.writer(sys.stdout)

# Header
writer.writerow(next(reader))

for row in reader:
    try:
        dataset, message, sent, _ = row
    except:
        sys.stderr.write(str(row))
        raise
    if sent == '':
        sys.stderr.write(dataset + '\n')
        os.system('echo "%s" | xclip')
        input()
        os.system("echo '%s' | xclip" % message)
        notes = input()
        sent = datetime.datetime.now().isoformat()
        newrow = dataset, message, sent, notes
        writer.writerow(newrow)
