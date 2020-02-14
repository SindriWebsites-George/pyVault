# Generates a password that contains letters, numbers, and special symbols
# then stores those passwords in a text file. The password is going to be
# 16 characters long.

from random import choice

def password():
    # ------------------------------------
    # The goal of this function is 
    # to provide a pseudo random
    # password for the user to use 
    # online without having to 
    # spend time thinking of a new one.
    # -------------------------------------
    
    # Giving the program a list of characters to use.
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    # Creating a place for the characters to be added
    password = ""
    
    for i in range(1, 16):
        password += choice(char)
        
    return password
   
