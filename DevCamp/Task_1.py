def main(): # Function Creation
    numbers = [] # Initializing array 'numbers'
    total = [0,0] # Initializing array 'total' with two indexes
    index = 0 # 'index' variable initialized to zero
    more = 'y' # 'More' variable initialized with string 'y'
    even = 0 # 'Even' variable to save the nuumber of even numbers
    odd = 0 # 'Odd' variable to save the number of odd numbers

    while more == 'y': # keep iterating as long as the user chooses to input another number,
        print ('Enter a positive number:') # promtp the user to input a number
        a = int(input()) 

        numbers.append(a) # appending the inputted numbers into the array
        index += 1 # increment index by 1
        

        more = input('Enter "y" to add another number or press the enter key to continue : ') # prompt the user to enter a number

    for x in numbers: # iterate for every x in 'numbers'
        if x % 2 == 0: # if the remainder of x divide by 2 is zero
            even += x # increment x (even)
        else:
            odd += x # else, increment x (odd)

    total[0] = even # assigning quantity of even numbers to the first index of 'total'
    total[1] = odd # assigning quantity of odd numbers to the second index of 'total'

    print('The Sum of Even and Odd you entered are: ') 
    print(total) # display the result


main()
