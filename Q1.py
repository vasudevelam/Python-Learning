# 1. Simple Billing System
def billing(amount):
    if amount>1000:
        discount=20
    elif amount>500:
        discount=10
    elif amount>200:
        discount=5
    else:
        discount=0
    total=amount-(amount*discount/100)
    return (total,discount)



amount=float(input("Enter the total amount : "))
print(billing(amount))