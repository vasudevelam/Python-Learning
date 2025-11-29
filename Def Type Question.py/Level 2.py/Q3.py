# Write a function to count how many vowels are in a string.

def vowles(String):
    count=0
    for i in String:
        if i=="aeiouAEIOU":
            count+=1
    return count

string=input("Enter a string is : ")    
print("Vowles are : ",vowles(string))