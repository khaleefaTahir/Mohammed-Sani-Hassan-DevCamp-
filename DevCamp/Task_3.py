def isPrime(num): # function creation
    # If given number is greater than 1
    if num > 1:
         
       # Iterate from 2 to n / 2  
       for i in range(2, num):
             
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0:
               return False
       else:
           return True
     
    else:
       return False
       
def getPrimeElements(str): # function creation 
    arr = str.split() # Split the string into a list
   
    tempPrimeElements = [] # tempPrimeElements elements are stored in an array
   
    for i in arr: # iterate for every element stored in variable arr.
        if isPrime(int(i)): # condition if it is a prime number
            tempPrimeElements.append(i) # append the tempPrimeElements to the array
   
    primeElements = list(dict.fromkeys(tempPrimeElements)) # returns a new dictionary as the keys of the dictionary
   
    return " ".join(primeElements) # return the prime numbers that were found
   
num = getPrimeElements(input("Enter numbers separated by space : "))
print("Prime numbers are " + num)
