# Level 2: Intermediate (Using loops, conditions)
# 🧠 Concepts: for, if-else, string and list handling


# Write a function that returns the factorial of a number.
def factorial(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fact=1
        for i in range(2,n+1):
            fact=fact*i
        return fact
    
number=int(input("Enter a number is : "))   
print("Factorial is : ",factorial(number))