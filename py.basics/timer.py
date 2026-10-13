import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

import time

my_time = int(input("Enter the time in seconds: "))

for x in reversed(range(1,my_time + 1, 1)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = x / 3600
    print(x)
    time.sleep(1)

print("Time's up!")