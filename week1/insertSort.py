# Source: https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#Source: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def inSort(arr):
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

# Source: https://www.tutorialspoint.com/How-do-we-use-file-readlines-to-read-multiple-lines-using-Python
def main(): 
    numFiles = file_len("data.txt") #saves number of lines

    with open("data.txt", 'r+') as f: #prints each line
        for line in f.readlines():
            tempLine = line.rstrip()
            tempArr = tempLine.split(" ")
            intArr = [int(num) for num in tempArr]

            intArr.pop(0) #ignores first number

            inSort(intArr)
            print(intArr)


if __name__ == "__main__":
    main()