# I used the Search() module of Regular Exprssions.

import re # Regular Expression syntax.

def validatePassword(password): # Function created with an argument. 
    flag = -1
    while True:  
        if re.search("^[a-zA-Z]+$", password): # Matches both upper and lower case letters of the english alphabet.
            flag = 0
            break 
        elif re.search("^[0-9]+$", password): # Matches any number from 0-9.
            flag = 1
            break
        elif re.search("^[0-9a-zA-Z]+$", password): # Matches both upper letters, lower letters and any number from 0-9.
            flag = 2
            break
        elif re.search("^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[_@.#&+-])([a-zA-Z0-9_@.#&+-]+)$", password): # Matches all type of letters, numbers and special characters. 
            flag = 3
            break
        elif re.search("\s", password): # Matches a single whitespace character.
            break
        else:
            break
    return flag # Return flag (Result)
   
password = validatePassword(input("Enter Password : ")) # Collecting input from the user

if password ==-1: # Password returns invalid if inputted password is not among all the above conditions. 
    print("Invalid Password")
elif password == 0:
    print("Very Weak Password") # Password returns 'very weak password' if password is only a string
elif password == 1:
    print("Weak Password") # Password returns 'weak password' if password is only a number
elif password == 2:
    print("Strong Password") # Password returns 'strong password' if password contains both a string and a number
elif password == 3:
    print("Very Strong Password") # Password returns 'very strong password' if password contains a string, number and a special character. 
else:
    print("Invalid Password")
