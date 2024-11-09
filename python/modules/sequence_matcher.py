from difflib import SequenceMatcher

def compare_sequence(a: str, b: str) -> float:
    sequence = SequenceMatcher(a=a, b=b)
    return sequence.ratio()

print(compare_sequence('abc', 'abcd'))