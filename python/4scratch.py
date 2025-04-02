from itertools import cycle, count
from time import sleep


def reverse_number(num):
    # Convert to string, reverse it, then convert back to int
    reverse = int(str(num)[::-1])
    return reverse

## Example usage:
print(reverse_number(1223))  # Output: 3221
print(reverse_number(987654321))  # Output: 123456789





