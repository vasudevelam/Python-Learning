 # Q2Temperature Checker

def weather(temp):
    if temp>35:
        return "Hot"
    elif temp>25:
        return "warm"
    elif temp>15:
        return "Cool"
    else:
        return "Cold"
    
temp=int(input("Enter a temperature is : "))
print(weather(temp))
    
