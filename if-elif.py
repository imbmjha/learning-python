# print Hello if 1 is stored in spam, Howdy if 2 is stored in spam, & Greetings if anything else stored in spam

spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
