# Write a function that returns both the minimum and maximum values from a list.
def min_max(lst):
    return min(lst), max(lst)

lst=eval(input("Enter a list is : "))   
minimum, maximum = min_max(lst)
print("Minimum is : ",minimum)
print("Maximum is : ",maximum)
