import os

def clearScreen():
    # -------------------------------
    # This function is added to allow
    # the program to work properly on
    # both windows and unix machines
    # by checking the name of the OS.
    # -------------------------------
    
    # gets the name of the OS
    name = os.name
    # print(name) # troubleshooting
    # Checks the version then clears 
    # the screen with the correct code
    if name == "nt":
        # Windows Machines
        os.system("cls")
    else:
        # Unix based Machines
        os.system("clear")

def dispMenu():
    # --------------------------
    # Prints a menu for the user 
    # to select from then returns
    # the user choice
    # ---------------------------
    
    # Makes sure that the screen is completely
    # cleared.
    clearScreen()
    
    #""" triple quates are for multi-line printing
    print("""
+--------------------------------+          
|  Welcome!                      |
|  Select your choice below.     |
|                                | 
|    1. Create a new Password    |
|    2. View Passwords           |
|                                |
|  Enter 'x' to quit             |
+--------------------------------+
          """)
    # Asks the user for their choice
    usrChoice = input("> Enter your choice:\n> ")
    return usrChoice

        