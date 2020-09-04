# importing Statistics module 
import statistics 
  
# creating a function that takes an array of positive integers
def main(pos_int = [1, 2, 3, 4, 5]):
    # Using the Standard Deviation Method in Statistic Module
    std_dev = statistics.stdev(pos_int)
  
    # Prints standard deviation 
    print("Standard Deviation of a is: ", std_dev)

main()
