def main(): # Function creation
    print('Enter a string, and the spaces will be replaced with "%20":') # Asking for user input
    a = input() # initializing user input to variable a 

    b = a.replace(' ', "%20") # using the replace() method to replcae any white space with %20
    print(b)
main()
