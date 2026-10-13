import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

# list comprehension examples
# SYNTAX:: doubles = [expression for value if iterable in condition]

# doubles = [x*2 for x in range(1,11)]
# [print(x) for x in doubles]

# numbers = [-1, 1, 2, -2, 5, -4, -5, 65, -45, 46, -76]
# positive_num = [num for num in numbers if num >= 0]
# print(positive_num)









