#QUES 3: input 4 digit number print sum
a=int(input("Enter a 4 digit number is : ="))
b=a//1000%10
c=a//100%10
d=a//10%10
e=a%10
r=b+c+d+e
print(" Sum of 4 digit number is : =",r)