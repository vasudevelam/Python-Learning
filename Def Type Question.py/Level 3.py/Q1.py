# Level 3: Advanced (Multiple parameters, default values, lists)

# Create a function with default argument (e.g., power function power(base, exp=2)).



# Write a function that removes all negative numbers from a list.
def remove_negatives(lst):
    for i in lst:
        if i<0:
            lst.remove(i)
            remove_negatives(lst)
    return lst

lst=eval(input("Enter a list is : "))
print("List after removing negative numbers : ",remove_negatives(lst))





