import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

#Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price of the food you just bought: "))
        foods.append(food)
        prices.append(price)

print("-"*10)
x = 0

for food, price in zip(foods,prices):
    print(f"Food: {food} - Price: ${price:.2}")

total = sum(prices)
print(f"Your total price is ${total:.2f}")

