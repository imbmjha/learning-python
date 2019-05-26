def greatest(x,y,z):
    if x > y and x > z:
        return "x is greater"
    if y > z:
        return f"{y} is greater"
    else:
        return f"{z} is greater"

num1 = int(input("enter 1st no= "))
num2 = int(input("enter 2nd no= "))
num3 = int(input("enter 3rd no= "))
greatest(num1,num2,num3)
print(greatest(num1,num2,num3))
