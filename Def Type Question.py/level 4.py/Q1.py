# Design a Python program for a small grocery store that helps calculate the total bill amount for a customer.

# The store sells a few fixed items. The program should:

# Display a list of items with their prices.

# Allow the customer to select an item by entering its number.

# Ask for the quantity.

# Use if, elif, and else statements to determine which item was selected.

# Calculate the total price for that item using the formula:

# total = price * quantity


# Display the item name, quantity, and total amount.

# If the user enters an invalid choice, display an error message.


print("Welcome to the Grocery Store!")
print("Here is the list of items available:")
def display_items():
    iteame=["1. Apples",
            "2. Bananas",
            "3. Oranges",
            "4. Grapes",
            "5. Mangoes"]
    prices=[100,
            120,
            60,
            40,
            80,]
    for i in range(len(iteame)):
        choice=int(input("Enter the item number you want to buy (1-5): "))
        quantity=int(input("Enter the quantity: "))
        if choice==1:
            total=100*quantity
            print("Quantity of Apples:",quantity,"Total Amount: $",total)
        elif choice==2:
            total=120*quantity
            print("Quantity of Bananas:",quantity,"Total Amount: $",total)
        elif choice==3:
            total=60*quantity
            print("Quantity of Oranges:",quantity,"Total Amount: $",total)
        elif choice==4:
            total=40*quantity
            print("Quantity of Grapes:",quantity,"Total Amount: $",total)
        elif choice==5:
            total=80*quantity
            print("Quantity of Mangoes:",quantity,"Total Amount: $",total)
        else:
            print("Invalid choice. Please select a valid item number.")
            return
        

print(display_items())