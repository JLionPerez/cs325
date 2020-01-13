# Title: HW 1 - Merge Sort
# Description: Sorts through arrays in a file and output results into a new file.
# Author: Joelle Perez
# Date: 15 January 2020

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
# Purpose: Runs all of the functions and the main parts of the program, such as reading in the files and translating each line into arrays.
# Arguments: none
# Returns: none
# Citation: https://www.tutorialspoint.com/How-do-we-use-file-readlines-to-read-multiple-lines-using-Python
def main():
    with open("data.txt", 'r+') as f: #prints each line
        for line in f.readlines():
            tempLine = line.rstrip() #removes newline
            tempArr = tempLine.split(" ") #removes spaces between each element
            intArr = [int(num) for num in tempArr] #change each element to integers
            intArr.pop(0) #ignores number size; first index

            mergSort(intArr) #call function to sort array

            strArr = ['{} '.format(str(string)) for string in intArr] #format to add spaces between each element
            out = open("merge.out", "a") #append to file instead of writing to save previous line
            for x in strArr:
                out.write(x)
            out.write("\n") #add newline to each line in file
            out.close()

# Runs the main function
if __name__ == "__main__":
    main()