age1 = int(input("enter the age of ram= "))
age2 = int(input("enter the age of ajay= "))
age3 = int(input("enter the age of shyam= "))
if age1 < age2 and age1 < age3:
    print(f"ram age {age1} is younger")
elif age2 < age3:
    print(f"ajay age {age2} is younger")
else:
    print(f"shyam age {age3} is yonger")        