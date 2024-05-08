nums = {1: 'a', 2: 'b'}


def sum_range(start, end):
    if start > end:
        start, end = end, start
    print(sum(range(start, end + 1)))


sum_range(10, 1)