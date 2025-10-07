#Q8 INPUT A WORDS WHEN WRITE STOP THEN PRINT ALL WORDS 
n=input("Enter a word: ")
a=[]
while n!="stop":
    a.append(n)
    n=input("Enter a word :  ")
for i in a:
    print(i)
