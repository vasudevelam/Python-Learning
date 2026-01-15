
# Write a function to check if a string is a palindrome.
def palindrome(s):
    return s == s[::-1]

s=input("Enter a string is : ")
print("Palindrome is : ",palindrome(s))