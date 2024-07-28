import pyinputplus



# any input after 5 seconds will throw an error, u can try to dypass it with try, except
try:
    inp = pyinputplus.inputStr(prompt = "What do now?", timeout = 5)
except pyinputplus.TimeoutException:
    pass


# or


inp = pyinputplus.inputStr(prompt = "What do now?", default = 'your_custom_string', timeout = 5)

# If the input is after 5 seconds, the function returns the value you set in default, in this case - "your_custom_string"