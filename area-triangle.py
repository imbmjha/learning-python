# find area of triangle

a = float(input("enter 1st side of triangle= "))
b = float(input("enter 2nd side of triangle= "))
c = float(input("enter 3rd side of triangle= "))
s = (a + b + c) / 2
area = s*( s - a)*(s - b)*(s - c)
print(f"area of triangle = {abs(area)}")
