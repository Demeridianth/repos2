# counting occurances

haystack = list(range(100))
needles = [1, 11, 111]

# 1
found = 0
for n in needles:
    if n in haystack:
        found += 1

# 2 using set
found = len(set(needles) & set(haystack))

# another way:
found = len(set(needles).intersection(haystack))