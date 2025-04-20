

sims = [1, 'abc', None, 4.05]

for s in sims:
    if isinstance(s, int | None):
        print(s)