def fizz_buzz(n):
    for i in range(n):
        if i % 5 == 0 and i % 3 == 0:
            print('fizz_buzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        print()        
        

# def fizz_buzz():
#     for i in range(0, 101):
#         print(i)
#         if i % 5 == 0 and i % 3 == 0:
#             print('fizz_buzz')
#         elif i % 3 == 0:
#             print('fizz')
#         elif i % 5 == 0:
#             print('buzz')
#         else:
#             print(i)


fizz_buzz(100)




