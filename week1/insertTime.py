# Title: HW 1 - Insertion Sort
# Description: Sorts through arrays in a file and output results into a new file.
# Author: Joelle Perez
# Date: 15 January 2020

import numpy as np
import time

# Function name: inSort()
# Purpose: Sort a passed array using an insertion sort.
# Arguments: integer array
# Returns: none
# Citation: Introduction to Algorithms by Thomas H. Cormen, Chapter 2 pg.18 - Insertion Sort Pseudocode
def inSort(arr):
    for j in range(1, len(arr)): #starts on the second, index arr[1]
        key = arr[j]
  
        i = j - 1
        while i >= 0 and key < arr[i]: 
                arr[i + 1] = arr[i]
                i -= 1
        arr[i + 1] = key

# Function name: main()
# Purpose: Runs all of the functions and the main parts of the program, such as randomizings arrays.
# Arguments: none
# Returns: none
# Citation: http://www.learningaboutelectronics.com/Articles/How-to-create-an-array-of-random-integers-in-Python-with-numpy.php
def main(): 
    n = 40000 #harcoded size, must change to get tests
    randArr = np.random.randint(0, 10000, n)

    inSort(randArr)
    print("Size of array is %s." % n)

# Runs the main function
if __name__ == "__main__":
    startTime = time.time()
    main()
    print("Time is %s seconds." % (time.time() - startTime))