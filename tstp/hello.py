# def print_hello():
#     print('Hello World')

def add_next(numbers):
    result = []
    for n in range(len(numbers)):
        for i in range(n + 1, len(numbers)):
            result.append(numbers[n] + numbers[i])
    return result

def multi(number1, number2):
    return number1 * number2

def not_ten(numbers):
    for n in numbers:
        if n != 10:
            return True
    return False


    