import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

menu = {
    "popcorn piccoli": 4.50,
    "popcorn medi": 5.50,
    "popcorn grandi": 6.50,
    "nachos con salsa": 6.00,
    "coca cola": 3.50,
    "acqua": 2.00,
    "m&m's": 3.00,
    "hot dog": 5.00
}

cart = []
total = 0

print("-"*10)
print("Welcome to our menù.")
print()

for key, value in menu.items():
    print(f"-- {key} : $ {value:.2f} --")
    print()

print("To place an order, just type the name of what you want.")
print()
print("When you are done with your order, just type in 'Ready' and you will get to the checkout window.")
print()

while True:
 product = input("Type here the name of the product: ").lower().strip()
 print()

 if product in menu.keys():
    cart.append(product)
    print(f"'{product}' is now in your cart.")
    price = float(menu.get(product))
    total = total + price

 elif product == "ready":
    break
 
 elif not product in menu.keys():
    print(f"'{product}' is not on our menù. Please check if you accidentally made any mistakes while typing. Thank you.")

print("-"*10)

if len(cart) > 0:

    print("Thank you for your order!")
    print()
    print("This is what you just ordered: ")

    for x in cart:
        print(f"-- '{x}' - Price: {menu.get(x)}")

    print(f"Your total is ${total:.2f}.")

else: 
   print("Thank you, have a good day")









