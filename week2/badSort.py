# Title: HW 2 - Bad Sort
# Description: 
# Author: Joelle Perez
# Date: 21 January 2020

# import numpy as np

def badSort(arr, n, a):
    if n == 2 and arr[0] > arr[1]:
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp

    elif n > 2:
        m = a * n
        badSort()

# def main():


# if __name__ == "__main__":
#     main()