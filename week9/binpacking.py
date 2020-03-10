# Title: HW 8 - Bin Packing
# Description: Find bins for the following functions.
# Author: Joelle Perez
# Date: 9 March 2020 (1 day late)

# Function name: first_fit()
# Purpose: Put each item as you come to it into the first (earliest opened) bin into which it fits. If there is no available bin then open a new bin.
# Arguments: integers, array
# Returns: integer
def first_fit(capacity, num_items, weights):
    num = 0
    bins = [capacity] * num_items #number of arrays

    for x in range(num_items): #for each item
        index = 0

        while index < num: #find bin
            if bins[index] >= weights[x]:
                bins[index] = bins[index] - weights[x]
                break
            index += 1

        if index == num: #if bin not found, find a new one
            bins[num] = capacity - weights[x]
            num += 1

    return num

# Function name: first_fit_decrease()
# Purpose: First sort the items in decreasing order by size, then use First-Fit on the resulting list.
# Arguments: integers, array
# Returns: integer
# Citations: https://www.w3schools.com/python/ref_func_sorted.asp
def first_fit_decrease(capacity, num_items, weights):
    return first_fit(capacity, num_items, sorted(weights, reverse=True))

# Function name: best_fit()
# Purpose: Place the items in the order in which they arrive. Place the next item into the bin which will leave the least room left over after the item is placed in the bin. If it does not fit in any bin, start a new bin.
# Arguments: integers, and array
# Returns: integer
def best_fit(capacity, num_items, weights):
    num = 0
    bins = [capacity] * num_items #number of arrays

    for i in range(num_items): #for each item
        index = 0
        minimum = capacity

        while index < num: #find fullest bin
            if bins[index] >= weights[i] and bins[index] - weights[i] < minimum:
                index_bin = index
                minimum = bins[index] - weights[i]
            index += 1

        if(minimum == capacity): #find a fuller bin
            bins[num] = capacity - weights[i]
            num += 1

        else:
            bins[index_bin] -= weights[i]

    return num

# Function name: main()
# Purpose: Runs all of the functions and the main parts of the program, such as reading in files and finding bins.
# Arguments: none
# Returns: none
def main():
    with open('bin.txt', 'r') as f:
        test_cases = int(f.readline().rstrip()) # number of test cases

        for i in range(test_cases):
            C = int(f.readline().rstrip()) # capacity

            total_items = int(f.readline().rstrip()) # number of items

            weights = list(map(int, f.readline().rstrip('\n').split(' '))) # list of weights

            # capture results
            ff_bins = first_fit(C, total_items, weights)
            dec_ff_bins = first_fit_decrease(C, total_items, weights)
            best_bins = best_fit(C, total_items, weights)

            # print output
            print("Test Case %d " % (i+1), end ="")
            print("First Fit: %d, " % ff_bins, end = "")
            print("First Fit Decreasing: %d, " % dec_ff_bins, end = "")
            print("Best Fit: %d" % best_bins)

#runs main and all it's programs
if __name__ == "__main__":
    main()