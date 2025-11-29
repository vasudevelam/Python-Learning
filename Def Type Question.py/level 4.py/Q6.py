# multiple functions crete table

def table(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
    
n=int(input("Enter a number to print table : "))
print("Table of ",n,"is : ")
table(n)