import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)
import exmodule # import the module

result = exmodule.squaring(3)
print(result)

