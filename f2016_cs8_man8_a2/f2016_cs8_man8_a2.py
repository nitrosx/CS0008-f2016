#
#
# name       : Max Novelli
# email      : man8@pitt.edu
# date       : 2016/10/31
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# This is the coding for the assignment #3 for class CS8 f2016
#
# We need to write a program that process as many files as the user will enter.
# Each file is a text file where each record is composed as it follow:
#
#  name,distance
#
# In each iteration of the loop, we need to ask for the file name,
# open the file, process the file by counting the lines and the sum of all the distances
# close the file and print the partial results.
# Once the iteration is over, we need to ask for the new file name.
# If the user enters a valid file name, we keep iterating.
# If the user enters "q","quit" or an empty string (by hitting enter), the main loop ends
# and we need to print the totals for the lines and the overall distance for all the files
#
# as a requirement, we need to define and use two functions:
# - printKV      : print a pair key, value in a consisten format
#                  key should be formatted as string of length equal to the maximum between klen and the length of key
#                  value should be formatted as string of length 20 if string, a 10 digits number with 3 decimal if float
#                  or a 10 digits if integer.
#                  Given the specs provided, I decided to format everything else as a string of length 20.
#
#                  function definition : printKV(key,value,klen)
#                  Input:
#                   - key   : key string to be printed
#                   - value : value to be printed following the key and ":"
#                   - klen  : size of key string to be printed
#                  Output:
#                   None
#
#
# - processFile: which iterate on all the lines of the file object and count the lines and
#                the total distance indicated in the second field of each record
#
#                function definition: [lines, totalDistance] = processFile(fh)
#
#                Input:
#                 - fh : file object of the input file
#
#                Output:
#                 - totalLines    : total number of lines in the file
#                 - totalDistance : total sum of the distances in each record of the file
#

import os.path

# contants
# length of the key
FORMAT_KEY_LENGTH = 30

#
# printKV function
def printKV(key,value,klen = 0):
    # check which is the length to be used when printing the key
    # max of klen and the length of key
    klen = max(klen,len(key));
    # check which is type of value and choose the proper formatting
    if isinstance(value,str):
        # we have a string
        fvalue = '20s'
    elif isinstance(value,float):
        # we have a float
        fvalue = '10.3f'
    elif isinstance(value,int):
        # we have a integer
        fvalue = '10d'
    else:
        # we do not know what we have,
        # so we try our best to convert it to a string and
        # format it as a string
        value = str(value)
        fvalue = '20s'
    # end if
    #
    # print key and value with correct formatting
    print(format(key,'>'+str(klen)+'s'),' : ',format(value,fvalue))
# end def

# processFile function
def processFile(fh):
    # count how many lines the files has and sum the distance that is the second field of each line
    #
    # initialize partial accumulators
    # partial total distance
    ptd = 0
    # partial total number of lines
    ptn = 0

    # loops on all the lines in the files
    # we hope that the read position is at the beginning of the file
    for line in fh:
        # in each iteration, we got the next line from the file
        #
        # remove new line (/n) and split in two parts: name and number
        [name, distance] = line.rstrip('\n').split(',')
        # convert distance from string to float
        distance = float(distance)
        # print name and distance in this record properly formatted
        printKV('Name', name, FORMAT_KEY_LENGTH)
        printKV('Distance', distance, FORMAT_KEY_LENGTH)
        #
        # update partial accumulators
        # partial total distance
        ptd += distance
        # partial total number of lines
        ptn += 1
    # for
    #
    # returns partials
    return [ptn, ptd]
#end def

# initialize totals partials
# total distance
td = 0
# total number of lines
tn = 0
# number of files
nf = 0

#
#  ask the user for the first file
print('Please enter the name of the first file to process.')
file = input('File name : ')

# check if file name is empty, or is q or quit and also if
while ( file != '' and file != 'quit' and file != 'q' and os.path.exists(file) ):

    # open the file in read mode and creates the file object
    fh = open(file, 'r')
    # process the file and get the number of lines and the sum of the distances
    ptn, ptd = processFile(fh)
    # close the file
    fh.close()

    # print partials properly formatted with spacing before and after
    print('')
    printKV('Partial Names found', ptn, FORMAT_KEY_LENGTH)
    printKV('Partial Distance', ptd, FORMAT_KEY_LENGTH)
    print('')

    # update total accumulators
    # number of files
    nf += 1
    # total distance
    td += ptd
    # total number of lines
    tn += ptn

    # ask the user the next file
    print('Please enter the name of the next file to process. Leave empty or type q/quit to exit')
    file = input('File name : ')

#while

# print report
print('')
printKV('Files read', nf, FORMAT_KEY_LENGTH)
printKV('Total Distance', td, FORMAT_KEY_LENGTH)
printKV('Names found', tn, FORMAT_KEY_LENGTH)
print('')
