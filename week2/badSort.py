# Title: HW 2 - Bad Sort
# Description: Sorts an integer array from least to greatest.
# Author: Joelle Perez
# Date: 21 January 2020

# Function name: badSort()
# Purpose: Sorts an array from least to greatest.
# Arguments: integer array, integer value
# Returns: none
def badSort(arr, a):
    n = len(arr)

    if n == 2 and arr[0] > arr[1]:
        #swaps arr[0] and arr[1]
        temp = arr[0] 
        arr[0] = arr[1]
        arr[1] = temp

    elif n > 2:
        m = int(a * n) #find mid

        tempArr = arr[0:m] #get subarray
        arr = tempArr
        badSort(arr, a)

        tempArr = arr[n - m:n] #subarray
        arr = tempArr
        badSort(arr, a)

        tempArr = arr[0:m] #subarray
        arr = tempArr
        badSort(arr, a)

# Function name: main()
# Purpose: Runs all of the functions and the main parts of the program, such as passing in the array in the function.
# Arguments: none
# Returns: none
def main():
    myArr = [21, 18, 32, 23]
    alpha = 1.0/2.0
    badSort(myArr, alpha)
    print(myArr)

# Runs main
if __name__ == "__main__":
    main()