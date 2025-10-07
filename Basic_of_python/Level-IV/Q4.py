#QUES Q4: inter a string count frequency
n=input("Enter a string is: =")
d={}
for char in n:
    if char in d:
        d[char]+=1
    else:
        d[char]=1
for char , count in d.items():
    print(f"'{char}': {count}")

