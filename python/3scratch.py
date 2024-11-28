

def get_user_input(prompt: str, converter=str) -> str:
        return converter(input(prompt))

test = get_user_input('enter for test: ')
print(test)