#Q6 Check Palindrome
def palindrome(a):
    a=str(a)
    rev=a[::-1]
    if a==rev:
        return True
    else:
        return False
    
a=input("Enter a string or number : ")
print(palindrome(a))

