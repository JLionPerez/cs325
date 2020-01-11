# Source: https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#Source: Introduction to Algorithms by Thomas H. Cormen, Chapter 2 pg.18 - Insertion Sort Pseudocode
def inSort(arr):
    for j in range(1, len(arr)): #starts on the second index arr[1]
        key = arr[j] 
  
        i = j - 1
        while i >= 0 and key < arr[i] : 
                arr[i + 1] = arr[i] 
                i -= 1
        arr[i + 1] = key 

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

            strArr = ['{0} '.format(str(string)) for string in intArr]

            out = open("insert.out", "a")
            for x in strArr:
                out.write(x)
            out.write("\n")
            out.close()


if __name__ == "__main__":
    main()