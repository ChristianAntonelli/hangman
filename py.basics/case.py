import os 
import subprocess
subprocess.run("cls" if os.name == 'nt' else "clear", shell = True)

def day_of_week(day):
    match day:
        case 1:
            return "It's Monday"
        case 2:
            return "It's Tuesday"
        case 3:
            return "It's Wednesday"
        case 4:
            return "It's Thursday"
        case 5:
            return "It's Friday"
        case 6:
            return "It's Saturday"
        case 7:
            return "It's Sunday"
        case _:
            return "Fuck off"

print(day_of_week("nigga"))
