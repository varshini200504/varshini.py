import math
n=int(input("enter num:"))
root=math.sqrt(n)
b=root*root
if n==b:
    print("perfect square")
else:
    print("not a perfect square")
