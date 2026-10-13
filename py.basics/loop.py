import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

for y in range(rows):
    for x in range(columns):
     print(symbol, end = "")
    print() #creates a new line(row)

