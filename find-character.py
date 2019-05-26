# to find no of occurance of a character in a string

name = input("enter your name")
occurance = 0
for char in name:
    
    if char.lower() == "a":
        occurance += 1
print(f"no of occurance = {occurance}")
        
        
