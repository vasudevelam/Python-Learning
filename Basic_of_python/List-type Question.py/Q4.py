# Take a list of integers and print all pairs of numbers whose sum is equal to a given target.
a=eval(input("Enter a number is : "))
tar=int(input('Enter a number is :'))
sum1=0
c=[]
for i in a:
    sum1=sum1+i
    c.append(sum1)
    if sum1==tar:
        print("Balance :")
    else:
        print("Not Balance:")

print(c)
    
        # print("TRaget is balance ",c)

        # print("notbalance the number",c)
