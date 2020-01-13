# Title: HW 1 - Insertion Sort
# Description: Sorts through arrays in a file and output results into a new file.
# Author: Joelle Perez
# Date: 15 January 2020

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

            inSort(intArr) #call function to sort array

            strArr = ['{} '.format(str(string)) for string in intArr] #format to add spaces between each element
            out = open("insert.out", "a") #append to file instead of writing to save previous line
            for x in strArr:
                out.write(x)
            out.write("\n") #add newline to each line in file
            out.close()

# Runs the main function
if __name__ == "__main__":
    main()