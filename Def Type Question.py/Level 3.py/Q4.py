# Define a function that reverses a string without using slicing.
def reverse_string(s):
    reversed_str=""
    for i in range(len(s)-1,-1,-1):
        reversed_str+=s[i]
    return reversed_str


s=input("Enter a string is : ")
print("Reversed string is : ",reverse_string(s))