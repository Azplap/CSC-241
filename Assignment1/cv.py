# Program to find coefficient 
# of variation of given array. 
import math 

# Function to find mean of 
# given array. 
def mean(arr, n): 
    sum = 0
    
    for i in range(0, n): 
        sum = sum + arr[i] 
    return (sum / n) 

# Function to find standard 
# deviation of given array. 
def standardDeviation(arr, n): 
    sum = 0
    
    for i in range(0, n): 
        sum = (sum + (arr[i] - mean(arr, n)) *
                    (arr[i] - mean(arr, n))) 

    return math.sqrt(sum / (n - 1)) 


# Function to find coefficient 
# of variation. 
def coefficientOfVariation(arr, n): 
    return (standardDeviation(arr, n) /
                        mean(arr, n)) 


# Driver Program 
# arr = [15, 36, 53.67, 25.45, 
#             67.8, 56, 78.09] 
# n = len(arr) 

# print(round(coefficientOfVariation(arr, n), 5)) 

# This code is contributed by Smitha Dinesh Semwal 
