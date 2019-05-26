# find no of vowel in a string

name = input("enter your name")
no_vowel = 0
for char in name:
    if char in 'aAeEiIoOuU':
        no_vowel += 1
    
print(f"No of vowels in { name } is { no_vowel }.")
