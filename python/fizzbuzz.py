def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print('fizz', end='')
        if i % 5 == 0:
            print('buzz', end='')

        print()


fizzbuzz(15)


