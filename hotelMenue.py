# Define menues
menue = {
    'Pizza' : 40,
    'Pasta' : 30,
    'Fries' : 30,
    'Burger': 60,
    'Coke' : 40,
}

print("Welcome to Eate and Eate Restorient")
print("Pizza : 40 \nPasta : 30\nFries : 30\nBurger: 60\nCoke  : 40")

orderTotal = 0
item_1 = input("Enter the name of item you to order = ")
if item_1 in menue:
    orderTotal+= menue[item_1]
    print(f"Your item {item_1} has added in your order")
else:
    print(f"Order item {item_1} is not in our menue")
anotherOrder = input("Do you want to add another item (yes/No)")
if anotherOrder == "yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menue: 
        orderTotal += menue[item_2]
        print(f"Item {item_2} hab been added")
    else:
        print(f"Orderd item {item_2} is not available")
print(f"the total amount of items is to pay {orderTotal} Rs")
