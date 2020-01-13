# Title: HW 1 - Merge Sort
# Description: Sorts through arrays in a file and output results into a new file.
# Author: Joelle Perez
# Date: 15 January 2020

import numpy as np
import time

# Function name: mergSort()
# Purpose: Sort a passed array using an merge sort.
# Arguments: integer array
# Returns: none
# Citation: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html
def mergSort(arr):
    arrLen = len(arr)
    i, j, k = 0, 0, 0

    if arrLen > 1:
        m = arrLen // 2 #divide in half
        lHalf = arr[:m] #sub-list of arr from the middle index to the very left index 
        rHalf = arr[m:] #sub-list of arr from the middle index to the very right index

        mergSort(lHalf) #sort the left side
        mergSort(rHalf) #sort the right side

        while i < len(lHalf) and j < len(rHalf):
            if lHalf[i] < rHalf[j]:
                arr[k] = lHalf[i] #main arr filled from least to greatest
                i += 1

            else:
                arr[k] = rHalf[j] 
                j += 1
                
            k += 1 #move to next index in main array

        while i < len(lHalf):
            arr[k] = lHalf[i] #adds in left sublist to main array
            i += 1
            k += 1

        while j < len(rHalf):
            arr[k] = rHalf[j] #adds in right sublist to main array
            j += 1
            k += 1

# Function name: main()
# Purpose: Runs all of the functions and the main parts of the program, such as randomizings arrays.
# Arguments: none
# Returns: none
# Citation: http://www.learningaboutelectronics.com/Articles/How-to-create-an-array-of-random-integers-in-Python-with-numpy.php
def main():
    n = 20000 #harcoded size, must change to get tests
    randArr = np.random.randint(0, 10000, n)

    mergSort(randArr)
    print("Size of array is %s." % n)

# Runs the main function
if __name__ == "__main__":
    startTime = time.time()
    main()
    print("Time is %s seconds." % (time.time() - startTime))