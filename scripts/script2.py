from script1 import *
import os 
import subprocess
## subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script 2!")
    favourite_food("pasta")
    favourite_drink("coffee")
    print("Goodbye")

if __name__ == "__main__":
    main()
    