from random_password import password
from os import path
from os import strerror
from menu import * 

def fileExists(fileName, usrPassword, masterFile):
    # --------------------------------------
    # This function checks to see if there
    # is already a file being used to store
    # a password. It also creates an archive
    # of previous passwords.
    # --------------------------------------
    
    # creating a name for the archive file.
    archive = "archive_" + fileName
    current = "current_" + fileName
    
    # Using the path.exists, we check to see
    # if there is already a password for that
    # program.
    if(path.exists(current)):
        # The '>' character is simply a styling
        # choice for displaying the text in the
        # terminal.
        print("> There is already a password associated with this program.")
        print("> Would you like to update the password?")
        try:
            # As long as no error occurs, the user will
            # be asked if they wish to continue with 
            # creating a new password. it is set to 
            # recognize 'y/n' or 'Y/N'. 
            usrInput = str(input("> (Y)es/(N)o\n> "))
            if(usrInput == "y") or (usrInput == "Y"):
                # We now open the file and write the 
                # new password to it.
                # 'fo' stands for File Open
                fo = open(current, "wt")
                fo.write(usrPassword)
                fo.close
                # We redifine the variable 'fo' here
                # and have it open the archive file
                fo = open(archive, "at")
                fo.write(usrPassword)
                fo.write("\n")
                fo.close
                print("> File written to succesfully.")
                input()
            elif(usrInput == "n") or (usrInput == "N"):
                input()
        except:
            # Reprint menu for user
            print("> Action failed, you are being taken to the main menu.")
            input()
    else:
        try:
            # Not much changes here from above
            # except that it will add the name
            # of the file to a master file for 
            # users to view to see all their 
            # programs/passwords.
            fo = open("list_of_programs.txt", "at")
            fo.write(masterFile)
            fo.write("\n")
            fo.close
            # The rest continues as normal
            # Writing to the current password
            # file.
            fo = open(current, "wt")
            fo.write(usrPassword)
            fo.close
            # Writing to the archive file.
            fo = open(archive, "at")
            fo.write(usrPassword)
            fo.write("\n")
            fo.close
            print("> File written to succesfully.")
            input()
        except IOError as e:
            print("> I/O Error Occured: ", strerror(e.errno))
            input()
        except:
            # Change to Main Menu here.
            print("> An Error has Occured.")
            input()

        

def newPassword(program):
    usrProgram = str(program)
    mstrFile = str(program)
    usrPassword = password()
    print("> Your password is:\n> ", usrPassword)
    
    name = (usrProgram + ".txt")
    fileExists(name, usrPassword, mstrFile)
    # print(name) # troubleshooting
    
# newPassword("Snapchat") # troubleshooting

def viewPassword():
    # -------------------------------
    # In this function we view
    # each program that the user
    # has a password for and asks
    # them which password they need.
    # --------------------------------
    
    # Opening and reading the programs listed
    # in the master list.
    fo = open("list_of_programs.txt", "r")
    if(fo.mode == "r"):
        programs = fo.read()
        print(programs)
    fo.close
    usrInput = str(input("> What password would you like to view?\n> This input is case sensitivie!\n> "))
    print("> Would you like to view older passwords also?")
    usrChoice = str(input("> (Y)es/(N)o\n> "))
    # Now we will try to open the file
    if(usrChoice == "y") or (usrChoice == "Y"):
        try:
            print("> Your passwords are:\n")
            fileChosen = "archive_" + usrInput + ".txt"
            # print(fileChosen) # troubleshooting
            fo = open(fileChosen, "r")
            if(fo.mode == "r"):
                filePassword = fo.read()
                print(filePassword)
                print("\n")
            fo.close
            input()
        except IOError as e:
            print("> I/O Error Occured: ", strerror(e.errno))   
            input()
        except:
            print("> An Error has Occured.")
            input()
    else:
        try:
            fileChosen = "current_" + usrInput + ".txt"
            fo = open(fileChosen, "r")
            if(fo.mode == "r"):
                filePassword = fo.read()
                print(filePassword)
            fo.close
            input()
        except IOError as e:
            print("> I/O Error Occured: ", strerror(e.errno))
            input()
        except:
            print(" An Error has Occured.")   
            input()
    
    
    