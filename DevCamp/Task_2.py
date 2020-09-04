def isPrime (): #Function creation
    a = int(input("input a number : ")) # Accepting input from the user to input a number of their choice
    if a > 1: # (A prime number cannot be 1 or less than 1)
        for i in range (2,a): # Iterate within the range of 2 and the number that the user inputted.
            if (a % i ) == 0: # if the remainder of this expression is 0, then it is not a prime number.
                print ("FALSE")
                break
        else:
            print ("TRUE")
    else:
        print ("FALSE")
     
isPrime()
