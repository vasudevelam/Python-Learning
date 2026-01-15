# n=int(input("Enter a number is :"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)
    

def fact(num):
    if (num==1):
        return 1
    else:
        return num*fact(num-1)
    
print(fact(5))