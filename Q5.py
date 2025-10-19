# Q5 Count Positive, Negative and Zero in a List
def pos_neg(n):
    Pos=0
    Neg=0
    ze=0
    for i in n:
        if i>0:
            Pos= Pos+1
        elif i<0:
            Neg=Neg+1
        else:
            ze=ze+1
    return Pos,Neg,ze  

n=eval(input("Enter a list of numbers : "))
print(pos_neg(n))


