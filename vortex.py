import os
from colorama import Fore, init
from art.main import print_banner
from art.menu import main_menu
init(autoreset=True)

file_name = "config.py"

def setup():
    print(Fore.RED + "Config file not found, creating one...")
    agree = input(Fore.YELLOW + "Do you agree to use this tool for educational purposes only? (y/n): ")
    if agree.lower() != "y":
        print(Fore.RED + "You must agree to continue. Exiting...")
        exit()
    
    install_requirements()
    create_config(True)

def install_requirements():
    print(Fore.CYAN + "Installing requirements...")
    os.system("pip install -r requirements.txt")
    print(Fore.GREEN + "Requirements installation completed!")

def create_config(installed=False):
    with open(file_name, "w") as f:
        f.write(f"agreed_to_terms = True\n")
        f.write(f"requirements_installed = {installed}\n")

def check_config():
    if not os.path.exists(file_name):
        setup()
    else:
        with open(file_name, "r") as f:
            lines = f.readlines()
        installed = any("requirements_installed = True" in line for line in lines)
        if not installed:
            install_requirements()
            create_config(True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_centered_banner():
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80  # default width
    banner = print_banner(ret=True)  # get banner as string instead of printing
    for line in banner.splitlines():
        print(line.center(width))

# ---- Main ----
check_config()
clear_screen()
print_centered_banner()
main_menu()
