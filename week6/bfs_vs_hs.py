# Title: HW 5 - Babyfaces vs. Heels
# Description: Determines whether it is possible or impossible to designate each wrestlers with rivals.
# Author: Joelle Perez
# Date: 16 February 2020

import sys

# Function name: No def functions, one driver. 
# Purpose: To go through each line of a file to gather wrestlers and assign each wrestler either as babyface or heels, and prints a yes or no depending if a pair of rivals have the same titles or not.
# Arguments: command line file
# Returns: none
# Citation: https://stackoverflow.com/questions/8280250/how-to-open-files-given-as-command-line-arguments-in-python
with open(sys.argv[1], 'r') as f:
    wrestlers = {}      #keys:values (name:title)
    flag = True         #initialize to true

    #for individual wrestlers
    numWrestlers = int(f.readline().rstrip())   #grab number of wrestlers
    for num in range(numWrestlers):   #only first wrestler will be a babyface
        name = f.readline().rstrip()    #name are keys

        if flag == False:
            title = ''
        else:
            title = 'babyface'

        flag = False    #rest of wrestlers will be unknown for now
        wrestlers[name] = title

    #for pairs (rivals)
    numRivals = int(f.readline().rstrip())  #grab number of rival pairs
    for num in range(numRivals):
        line = f.readline().rstrip()

        rivalry = [str(x) for x in line.split()]    #each pair (line) will be its own array
        r1 = rivalry[0]
        r2 = rivalry[1]

        if wrestlers[r1] == 'babyface' and wrestlers[r2] == '':    #if wrestler is babyface then rival is heel
            wrestlers[r2] = 'heel'

        elif wrestlers[r1] == 'heel' and wrestlers[r2] == '':  #vice versa
            wrestlers[r2] = 'babyface'

        elif wrestlers[r1] == '' and wrestlers[r2] == '':  #if both wrestlers do not have titles, the first will be babyface the second will be heel
            wrestlers[r1] = 'babyface'
            wrestlers[r2] = 'heel'

        elif wrestlers[r1] == '' and wrestlers[r2] != '':  #if one of the wrestlers has a title give the other wrestler the opposite title
            if wrestlers[r2] == 'heel':
                wrestlers[r1] = 'babyface'

            else:
                wrestlers[r1] = 'heel'

        elif wrestlers[r1] != '' and wrestlers[r2] == '': #vice versa
            if wrestlers[r1] == 'babyface':
                wrestlers[r2] = 'heel'

            else:
                wrestlers[r2]: 'babyface'

        elif wrestlers[r1] == 'babyface' and wrestlers[r2] == 'babyface': # (impossible) if both wrestlers have the same titles, it means there is not enough wrestlers to rival with
            exit('No')

        elif wrestlers[r1] == 'heel' and wrestlers[r2] == 'heel': #same for heels
            exit('No')

    #arrays to gather wrestlers
    babyfaces = []
    heels = []

    for wrestler in wrestlers: #add into proper lists
        if wrestlers[wrestler] == 'babyface':
            babyfaces.append(wrestler)

        else:
            heels.append(wrestler)

    print('Yes')    #possible

    print('Babyfaces:', end=" ")    #print out babyfaces
    for wrestler in babyfaces:
        print(wrestler, end=" ")

    print('\nHeels:', end=" ")  #print out heels
    for wrestler in heels:
        print(wrestler, end=" ")

    print('')