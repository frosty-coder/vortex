import os
from colorama import Fore, init
from art.main import print_banner
from art.menu import main_menu
from tools.maintain import clear_screen, input_prompt
from phishing.menu import phishing_menu
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



check_config()
clear_screen()
print_banner()
main_menu()

def exit_program():
    print(Fore.RED + "Exiting...")
    exit()

def invalid_option():
    print(Fore.RED + "Invalid option, please try again.")
    main_menu()



while True:
    user_choice = input_prompt()
    if user_choice == "1":
        print(Fore.GREEN + "You selected PHISHING.")
        # Placeholder for PHISHING functionality
    elif user_choice == "2":
        print(Fore.GREEN + "You selected MALWARE KIT.")
        # Placeholder for MALWARE KIT functionality
    elif user_choice == "3":
        print(Fore.GREEN + "You selected SIM / GMAIL hacks.")
        # Placeholder for SIM / GMAIL hacks functionality
    elif user_choice == "4":
        print(Fore.GREEN + "You selected SPY KIT.")
        # Placeholder for SPY KIT functionality
    elif user_choice == "99":
        exit_program()
    else:
        invalid_option()