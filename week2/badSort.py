# Title: HW 2 - Bad Sort
# Description: 
# Author: Joelle Perez
# Date: 21 January 2020

def badSort(arr, a):

    print(arr)
    print("a: ", a)

    n = len(arr)
    print("length: ", n)
    if n == 2 and arr[0] > arr[1]:
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp

    elif n > 2:
        m = int(a * n)
        print("m: ", m)

        tempArr = arr[0:m]
        arr = tempArr

        print("1. Original array: ", arr)
        print("1. Temp array: ", tempArr)

        badSort(arr, a)

        tempArr = arr[n - m:n]
        arr = tempArr

        print("2. Original array: ", arr)
        print("2. Temp array: ", tempArr)

        badSort(arr, a)

        tempArr = arr[0:m]
        arr = tempArr

        print("3. Original array: ", arr)
        print("3. Temp array: ", tempArr)

        badSort(arr, a)

def main():
    myArr = [21, 18, 32, 23]
    alpha = 1.0/2.0
    badSort(myArr, alpha)
    print(myArr)


if __name__ == "__main__":
    main()