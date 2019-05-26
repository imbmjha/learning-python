cp = int(input("enter cost price= "))
sp = int(input("enter selling price= "))
if sp > cp:
    profit = sp - cp
    percent = (profit / cp) * 100
    print(f"profit =  {profit}")
    print(f"profit% = {percent}")
elif cp > sp:
    loss = cp - sp
    percent = (loss / cp) * 100
    print(f"loss = {loss}")
    print(f"loss%= {percent}")