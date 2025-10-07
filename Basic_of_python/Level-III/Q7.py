#QUES 7: input in side using her fr 
import math
a=float(input("Enter a 1 side is : ="))
b=float(input("Enter a 2 side is : ="))
c=float(input("Enter a 3 side is : ="))
s=(a+b+c/2)
t=(math.sqrt(s*s-a)*(s-b)*(s-c))
print(s)
print(t)
