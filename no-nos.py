import string
# find no. of numbers in a string

name = input("enter your name= ")
no_nos = 0
no_char = 0
for numbers in name:
    if numbers in string.digits:
        no_nos += 1
        
        
print(f"total no of nos= {no_nos}")