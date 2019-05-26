# triangle valid by angle

angle1 = int(input("enter first angle= "))
angle2 = int(input("enter second angle= "))
angle3 = int(input("enter third angle= "))

triangle = angle1 + angle2 + angle3
if triangle == 180:
    print(f"it forms triange= {triangle}")
else:
    print(f"it doesn't form triangle= {triangle}")
