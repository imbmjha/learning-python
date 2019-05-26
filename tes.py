def fizz_buz(fizz_buzz):
    if fizz_buzz % 3 == 0:
        return ('fizz')
    elif fizz_buzz % 5 == 0:
        return ("buzz")
    elif fizz_buzz % 15 == 0:
        return ("fizzbuzz")
    else :
        return


x = fizz_buz(int(input()))
print(x)