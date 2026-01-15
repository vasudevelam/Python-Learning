# Electricity Bill Generator crete a function less 0 to 100 units is For the first 100 units → ₹5 per unit

# For the next 100 units (101–200) → ₹7 per unit

# For units above 200 → ₹10 per unit

# The program should:

# Take customer name and total units consumed as input.

# Calculate the total electricity bill based on the above rates.

# Display the customer name, units consumed, and total bill amount in a proper format.



def electricity_bill():
    name=input("Enter a customer name is : " )
    units=int(input("Enter the total units consumed is : "))
    if units<=100:
        bill=units*5
    elif units>100 and units<=200:
        bill=units*7
    else:
        bill=units*10
    print("\n------ Electricity Bill ------")
    print(f"Customer Name : {name}")
    print(f"Units Consumed : {units}")
    print(f"Total Bill Amount : ₹{bill}")
    print("-------------------------------")
    # return "\n------ Electricity Bill ------"
    # return "Customer Name :", name
    # return"Units Consumed : ",units                           #this not working
    # return "Total Bill Amount :", bill
    # return"-------------------------------"


    


print(electricity_bill())
    