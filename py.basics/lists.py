import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

fruits = ["Pear", "Coconut", "Banana", "Peach"] #This is a list.

fruits[1] = "Cherry" # Takes the place of the previous value.
fruits.insert(1, "Strawberry") # Inserts a new element while the previous one shifts up in places
fruits.append("Pineapple") # Appends a new element a the end of the list

fruits.sort(reverse = True)

for fruit in fruits:
    print(fruit)


