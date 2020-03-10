import timeit

def first_fit(capacity, num_items, weights):
    num = 0
    temp_cap = capacity
    bins = [capacity] * num_items

    for x in range(num_items):
        index = 0

        while index < num:
            if bins[index] >= weights[x]:
                bins[index] = bins[index] - weights[x]
                break
            index += 1

        if index == num:
            bins[num] = temp_cap - weights[x]
            num += 1

    return num

#https://www.w3schools.com/python/ref_func_sorted.asp
def first_fit_decrease(capacity, num_items, weights):
    return first_fit(capacity, num_items, sorted(weights, reverse=True))

def best_fit(capacity, num_items, weights):
    num = 0
    # temp_cap = capacity
    bins = [capacity] * num_items

    for x in range(num_items):
        index = 0
        minimum = capacity
        bin_index = 0

        while index < num:
            if bins[index] >= weights[x] and bins[index] - weights[x] < minimum:
                bin_index = index
                minimum = bins[index] - weights[x]
            index += 1

        if minimum == capacity:
            bins[num] = capacity - weights[x]
            num += 1

        else:
            bins[bin_index] -+ weights[x]

    return num

def main():
    with open('bin.txt', 'r') as inFile:
        # Read in the number of test cases
        line = int(inFile.readline().rstrip())

        # Loop through the range of test cases
        for x in range(line):
            # Read in the capacity of each bag
            capacity = int(inFile.readline().rstrip())

            # Read in the number of items
            item_total = int(inFile.readline().rstrip())

            # Create an array from the line of integers (this represents the weight of each item)
            item_weights = list(map(int, inFile.readline().rstrip('\n').split(' ')))

            # Pass in each variable to the three algorithms and grab their results
            first_fit = firstFit(capacity, item_total, item_weights)
            decreasing_first_fit = firstFitDecreasing(capacity, item_total, item_weights)
            best_fit = bestFit(capacity, item_total, item_weights)

            # Capture time for each function
            ff_start = timeit.default_timer()
            firstFit(capacity, item_total, item_weights)
            ff_end = timeit.default_timer()
            ff_time = (ff_end - ff_start)

            ffd_start = timeit.default_timer()
            firstFitDecreasing(capacity, item_total, item_weights)
            ffd_end = timeit.default_timer()
            ffd_time = (ffd_end - ffd_start)

            bf_start = timeit.default_timer()
            bestFit(capacity, item_total, item_weights)
            bf_end = timeit.default_timer()
            bf_time = (bf_end - bf_start)

            print("--- Test case %d ---" % (x + 1))
            print("\tFirst-Fit:")
            print("\t\tBins: %d, Time: %0.10f\n" % (first_fit, ff_time))
            print("\tFirst-Fit-Decreasing:")
            print("\t\tBins: %d, Time: %0.10f\n" % (decreasing_first_fit, ffd_time))
            print("\tBest-Fit:")
            print("\t\tBins: %d, Time: %0.10f\n" % (best_fit, bf_time))