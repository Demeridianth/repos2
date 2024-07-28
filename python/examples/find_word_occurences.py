# fetch and update a list of word occurrences from the index i a text file

import re
import sys

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    # sys.argv[] takes a text file as an argument in command line: "python3 1scratch.py zen.txt"
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences 

# for word in sorted(index, key=str.upper):
#     print(word, index[word])


#better version with dict.setdefault()

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
 for line_no, line in enumerate(fp, 1):
    for match in WORD_RE.finditer(line):
        word = match.group()
        column_no = match.start() + 1
        location = (line_no, column_no)
        index.setdefault(word, []).append(location)


# display in alphabetical order
# for word in sorted(index, key=str.upper):
#     print(word, index[word])



# my_dict.setdefault(key, []).append(new_value)

# is the same as:

# if key not in my_dict:
#   my_dict[key] = []
#   my_dict[key].append(new_value)



""" defaultdict: Another Take on Missing Keys """
import collections

index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
 for line_no, line in enumerate(fp, 1):
    for match in WORD_RE.finditer(line):
        word = match.group()
        column_no = match.start() + 1
        location = (line_no, column_no)
        index[word].append(location)


# display in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
