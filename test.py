import string
# find no of uppercase letter

name = input("enter a string= ")
upper_case = 0
lower_case = 0
for char in name:
    if char in string.ascii_uppercase:
       upper_case += 1
    elif char in string.ascii_lowercase:
        lower_case += 1

print(f"no of uppercase letter in {name} is {upper_case}")
print(f"no of lowercase letter in {name} is {lower_case}")
    