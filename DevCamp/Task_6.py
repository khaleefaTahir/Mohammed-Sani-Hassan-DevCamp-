# Creating a function with two parameters, a and b.
def main(a = [1, 2, 3, 4, 5, 6], b = 6):

    # using if-statements to determine the three array indexes that add up to the number in the second parameter
    if (a[0] + a[1] + a[2]) == b:
        c = [a[0],a[1],a[2]]
        print(c)

    elif (a[1] + a[2] + a[3]) == b:
        c = a[1] + a[2] + a[3]
        print(c)
        
    elif (a[2] + a[3] + a[4]) == b:
        c = a[2] + a[3] + a[4]
        print(c)

    elif (a[3] + a[4] + a[5]) == b:
        c = a[3] + a[4] + a[5]
        print(c)
    # Returns -1 when three indexes do not add up to the number in the second parameter.
    else:
        return -1
    

main()
