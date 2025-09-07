import os
from colorama import Fore, init

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
def input_prompt():
    choice = input(Fore.YELLOW + "zerostack@v1:-/vortex#> ")
    return choice