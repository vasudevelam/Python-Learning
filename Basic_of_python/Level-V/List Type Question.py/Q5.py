a = eval(input("Enter a list of numbers: "))  
b = len(a)
c = max(a)
ind = a.index(c)

if ind < b / 2:
    print("1st half")
else:
    print("2nd half")

print("INdex",ind)