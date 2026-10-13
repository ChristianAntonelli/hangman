import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

num_pad = (
    ("1","2","3"),
    ("4","5","6"),
    ("7","8","9"),
    ("*","0","#")
)

for tpl in num_pad:
    for x in tpl:
        print(x, end=" ")
    print()





