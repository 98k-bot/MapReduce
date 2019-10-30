from operator import itemgetter
import sys

current_word = None
current_date = None
current_count = 0
current_count_date = [0,0,0,0,0,0,0,0,0,0,0,0]
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    try:
        date, other = line.split("\t",1)
        word, count = other.split("\t",1)
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
        current_date = date[:2]
        if current_date == '01':
            current_count_date[0] +=count
        elif current_date =='02':
            current_count_date[1] += count
        elif current_date =='03':
            current_count_date[2] += count
        elif current_date =='04':
            current_count_date[3] += count
        elif current_date =='05':
            current_count_date[4] += count
        elif current_date =='06':
            current_count_date[5] += count
        elif current_date =='07':
            current_count_date[6] += count
        elif current_date =='08':
            current_count_date[7] += count
        elif current_date =='09':
            current_count_date[8] += count
        elif current_date =='10':
            current_count_date[9] += count
        elif current_date =='11':
            current_count_date[10] += count
        else:
            current_count_date[11] += count

    else:
        if current_word:
            # write result to STDOUT
            print("%s\t%s" % (current_word, current_count_date))
        current_count = count
        current_word = word
        current_date = date[:2]
# do not forget to output the last word if needed!
if current_word == word:
    print("%s\t%s " % (current_word, current_count_date))
