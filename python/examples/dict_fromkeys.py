x = [1, 2, 3]

this_dict = dict.fromkeys(x).values()
# >>> dict_values([None, None, None])
this_dict = dict.fromkeys(x).keys()
# >>> dict_keys([1, 2, 3])

y = 0
this_dict = dict.fromkeys(x, y)
# >>> {1: 0, 2:0, 3:0}