#Q10 Convert Lowercase to Uppercase
def upper1(text):
    list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    result=""
    for ch in text:
        if ch in list1:
            index=list1.index(ch)
            result=result+list2[index]
        else:
            result= result+ch
    return result

text=input("Enter a string : ")
print(upper1(text))

