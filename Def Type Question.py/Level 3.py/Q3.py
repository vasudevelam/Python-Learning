# Create a function that counts how many even and odd numbers are in a list.
def count_even_odd(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=eval(input("Enter a list is : "))
print("Even and Odd count is : ",count_even_odd(lst))
