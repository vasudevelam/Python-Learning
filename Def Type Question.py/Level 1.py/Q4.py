# Write a function that checks if a number is even or odd.
def even_odd(number):
    if number%2==0:
        return "Even number "
    else:
        return "Odd number "
    
number=int(input("Enter a number is : "))
print(even_odd(number))