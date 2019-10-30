import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    print ("%s\t%s\t%s" % (words[1],words[7], 1))