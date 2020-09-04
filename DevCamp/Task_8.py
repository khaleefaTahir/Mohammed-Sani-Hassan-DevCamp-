# creating global variable nums
nums = []

def count_3s(n):
    count = 0
    #traversing from 0 through n
    while (n > 0):
        if (n % 10 == 3) or (n/10==3):
            #appending n to the global variable
            nums.append(n)
            #incrimenting the counter
            count = count + 1
        n = int(n / 10) 
    return count

def count_in_range(n):
    count = 0 # setting variable 'count' to zero
    for i in range(2,n): # Iterate through 2 to n
        count = count + count_3s(i)
    return count

number = int(input('Enter the number : '))
number +=1 # increment number
print('count: ', count_in_range(number), ' Numbers: ', nums)
