from colorama import Fore, init
from tools.maintain import clear_screen, input_prompt

def menu():
    print(Fore.CYAN + """
===========================================
|           Phishing Menu                |
===========================================
| 1. self manage Phishing Pages          |
| 2. default Phishing Pages              |
| 3. Back to Main Menu                   |
===========================================
"""
)
def self_menu():
    print(Fore.CYAN + """
===========================================
|           self Menu                |
===========================================
| 1. Create Phishing Page                |
| 2. Manage Phishing Pages               |
| 3. View Logs                           |
| 99. Back to Main Menu                  |
===========================================
        ==========================
""")
    
def default_menu():
    print(Fore.CYAN + """
===========================================
|           default Menu                |
===========================================
| 1. list Phishing Pages                 |
| 2. Manage Phishing Pages               |
| 3. View Logs                           |
| 99. Back to Main Menu                  |
===========================================
        ==========================
""")

def phishing_page():
    print(Fore.GREEN + """
===========================================
|    list of available Phishing Page...   |
===========================================
| 1. Facebook       |2. Instagram         |
| 3. Google         |4. Netflix           |
| 5. Twitter        |6. Paypal            |
| 7. Microsoft      |8. Yahoo             |
| 9. Snapchat       |10. Ebay             |
| 11. Github        |12. Wordpress        |
| 13. Protonmail    |14. Tiktok           |
===========================================
          
          """)
def list_phishing_pages():
    print(Fore.GREEN + "Listing Phishing Pages...")
    phishing_page()
    
    
def phishing_menu():
    while True:
        menu()
        choice = input_prompt()
        if choice == "1":
            self_menu()
            sub_choice = input_prompt()
            if sub_choice == "1":
                print(Fore.GREEN + "Creating Phishing Page...")
                # Add your code here
            elif sub_choice == "2":
                print(Fore.GREEN + "Managing Phishing Pages...")
                # Add your code here
            elif sub_choice == "3":
                print(Fore.GREEN + "Viewing Logs...")
                # Add your code here
            elif sub_choice == "99":
                continue
            else:
                print(Fore.RED + "Invalid option, please try again.")
        elif choice == "2":
            default_menu()
            sub_choice = input_prompt()
            if sub_choice == "1":
                print(Fore.GREEN + "Listing Phishing Pages...")
                # Add your code here
            elif sub_choice == "2":
                print(Fore.GREEN + "Managing Phishing Pages...")
                # Add your code here
            elif sub_choice == "3":
                print(Fore.GREEN + "Viewing Logs...")
                # Add your code here
            elif sub_choice == "99":
                continue
            else:
                print(Fore.RED + "Invalid option, please try again.")
        elif choice == "3":
            break
        else:
            print(Fore.RED + "Invalid option, please try again.")
    