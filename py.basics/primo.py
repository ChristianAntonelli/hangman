#username must not contain digits
#username must not contain spaces
#usernam must not be longer than 12 characters


import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)


while True:

    username = input("Type in your username: ")

    if len(username) > 12:
        print("Your username is too long and should not exceed 12 characters!")
    elif not username.isalpha():
        print("Your username can't cointain either digits or spaces!")
    else:
        print(f"Congrats, your just logged in as {username}!")
        break
