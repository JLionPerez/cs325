# Title: HW 3 - Bottom-up Dynamic Programming for Knapsack
# Description: Solves the knapsack problem in bottom up dynamic programming approach.
# Author: Joelle Perez
# Date: 27 January 2020 

# Function name: bu_knapsack()
# Purpose: Finds the optimal subset value.
# Arguments: integer arrays, and integers
# Returns: integer
# Citation: https://www.sanfoundry.com/python-program-solve-0-1-knapsack-problem-using-dynamic-programming-bottom-up-approach/
def bu_knapsack(weight, value, W):
    n = len(value) - 1
 
    # m[i][w] will store the maximum value that can be attained with a maximum
    # W of w and using only the first i items
    m = [[-1]*(W + 1) for _ in range(n + 1)]
 
    # will always be 0 at 0th index
    for w in range(W + 1):
        m[0][w] = 0 
 
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weight[i] > w:
                m[i][w] = m[i - 1][w] #current value will get the value previous
            else:
                m[i][w] = max(m[i - 1][w - weight[i]] + value[i], m[i - 1][w])
 
    return m[n][W]

# Function name: main()
# Purpose: Opens file and reads data
# Arguments: none
# Returns: none
def main():
    with open('data.txt', 'r') as f:
        fileStr = [int(num) for line in f for num in line.split()]

    vals = [fileStr[i] for i in range(len(fileStr)) if i % 2 != 0]
    weights = [fileStr[i] for i in range(len(fileStr)) if i % 2 == 0]

    print(bu_knapsack(weights, vals, 6))

# runs main
if __name__ == "__main__":
    main()
