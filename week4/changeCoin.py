# Title: HW 4 - Coin Change Greedy Algorithm
# Description: Finds the minimum amount of coins to satisfy desired amount.
# Author: Joelle Perez
# Date: 4 January 2020 (1 day late)
import collections

# Function name: greedyCoin()
# Purpose: Uses greedy approach to find minimum coins.
# Arguemnts: integer and arrays
# Returns: greedyCoin()
def greedyCoin (amount, coins, purse):
    length = len(coins)
    for i in range(length, 0, -1): #start from the end of list
        cent = coins[i - 1] #grab current position
    
        if amount >= cent:
            purse.append(cent) #add to purse
            return greedyCoin(amount - cent, coins, purse) #repeat until amount is less than cents

# Function name: main()
# Purpose: Runs all of the functions and the main parts of the program, such as reading in the files and translating each line into strings.
# Arguments: none
# Returns: none
# Citation: https://www.tutorialspoint.com/How-do-we-use-file-readlines-to-read-multiple-lines-using-Python
#           https://www.geeksforgeeks.org/count-frequencies-elements-array-python-using-collections-module/
def main():
    with open("data.txt", 'r+') as f: #prints each line
            for line in f.readlines():
                tempLine = line.rstrip() #removes newline
                tempArr = tempLine.split(" ") #removes spaces between each element
                intArr = [int(num) for num in tempArr] #change each element to integers

                c = intArr[0] 
                k = intArr[1]
                n = intArr[2]
                realCoins = [] #will hold denominations from c and k

                for x in range(k + 1): #each c^k gets appended to realCoins
                    realCoins.append(c**x) 

                coinPurse = [] #captures coins used
                greedyCoin(n, realCoins, coinPurse)

                freq = collections.Counter(coinPurse) #get frequencies for each element

                out = open("change.txt", "a") #append to file instead of write to keep every line

                for key, value in freq.items(): #for each item write into file
                    strN = "{} {}".format(key, value)
                    out.write(strN)
                    out.write("\n")
                out.close()

# Runs the main function
if __name__ == '__main__':
    main()