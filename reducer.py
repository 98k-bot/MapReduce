from operator import itemgetter
import sys

current_word = None
current_area = None
current_count = 0
largest_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    try:
        word, other = line.split("\t",1)
        area, count = other.split("\t",1)
    except ValueError:
        continue
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s\t%s' % (current_word, current_area, current_count))
        if current_count>largest_count:
            print("most of the crime happening in %s for %s times, the type is %s" % (current_area, current_count, current_word))
            largest_count = current_count
        current_count = count
        current_word = word
        current_area = area

# do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s\t%s' % (current_word, current_area, current_count))
if current_count > largest_count:
    print(
        "most of the crime happening in %s for %s times, the type is %s" % (current_area, current_count, current_word))
    largest_count = current_count