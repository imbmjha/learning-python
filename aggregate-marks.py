#find aggregate marks and percentage of 5 different subject

sub1 = int(input("enter the marks of maths= "))
sub2 = int(input("enter the marks of physics= "))
sub3 = int(input("enter the marks of chemistry= "))
sub4 = int(input("enter the marks of hindi= "))
sub5 = int(input("enter the marks of english= "))
aggregate_marks = (sub1+sub2+sub3+sub4+sub5)/5
print(f"aggregate marks = {aggregate_marks}")
percent = (sub1+sub2+sub3+sub4+sub5)/500*100
print(f"percentage % = {percent}")