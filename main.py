from menu import *
from file_management import viewPassword
from file_management import newPassword

# Displays the menu then stores the returned value
# to be checked in the while loop below.
choice = dispMenu()

while (choice != "x"):
    if choice == "1":
        usrInput = str(input("> Enter the Name of the Program: \n> "))
        newPassword(usrInput)
    elif choice == "2":
        viewPassword()
    else: 
        print("You've entered an inccorect choice")
    
    choice = dispMenu()

print("> Thank you for using this program!")
input()