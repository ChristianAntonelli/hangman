
import os 
import subprocess
## subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

def favourite_food(food):
    print(f"Your favourite food is {food}")

def main():
    print("This is Script1")
    favourite_food("pizza")
    print("Goodbye")

if __name__ == '__main__':
    main()
