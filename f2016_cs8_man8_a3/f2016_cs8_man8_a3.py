#
#
# name       : Max Novelli
# email      : man8@pitt.edu
# date       : 2016/10/31
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Assignment #3
#
# Description:
# A customer needs to process a number of text files (called data files) that contain names and distance run by study participants.
# The format of those files is as follows:
#
# Max ,34.23
# Barbara ,23.00
# Luka ,12.87
# …
#
# In those files, each row is a comma separated list of 2 values: the first one is the name of the participant and the
# second is the distance that the participant has run.
# The names of the input files are stored one per line in an additional file, called the master input list.
# This file has the following structure:
#
# <data file 1>
# <data file 2>
# <data file 3>
# …
#
# Write a program that read the master input list file, retrieves the names of the data files and from each one of them
# reads every line, extract name and distance. Once the program has all the data in memory, it has to compute the following
# quantities and informations:
# - number of files read in input
# - total number of lines read
# - total distance run (aka the sum of all the distances loaded from provided files)
# - total distance run for each individual participant
# - individual maximum distance run and by which participant
# - individual minimum distance run and by which participant
# - report if there are any participants that appears more than once, how many times and their names
# - total number of participants
#
# The program should provide an terminal output similar to the following:
#
#	Number of Input files read   : xx
#	Total number of lines read   : xx
#
#	total distance run           : xxxx.xxxxx
#
#	max distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	min distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	Total number of participants : xx
#	Number of participants
#    with multiple records       : xx
#
# The program should also create an output file reporting name of the participant, how many times their name appears in
# the input files and the total distance run. Each row should be as follows:
#
# Max,3,124.23
# Barbara,2,65.00
# Luka,1,12.87
# …
#

#
# function getDataFromFile(file)
# read all the lines from the file, remove first line (header) and split all the others in name and distance
# insert a dictionary with name and distance in output list
#
# Input:
#  - file: (string) data file name
#
# Output
#  - data: (list) list of dictionaries, with each dictionary defined as follow:
#          { 'name': <participant_name>, 'distance' : <distance_run> }
#  - nlines: (integer) number of lines read from the file
def getDataFromFile(file):
    # initialize output list
    output = []
    # initialize number of lines read
    nlines = 0;
    # read file line by line
    for line in open(file,'r'):
        # update number of lines read
        nlines += 1
        # exclude first line that is the header
        # we can recongize it because it contains the word "distance"
        if "distance" in line:
            # skip line
            continue
        # remove \n ending the line and split line at ","
        temp1 = line.rstrip('\n').split(',')
        # use try/except to avoid unhendled errors
        try:
            # append record to output list in the form of a dictionary with 2 keys: name and distance
            # remove unwanted spaces from name and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            # here we catch all the lines that are incorrectly formatted
            # and we skipp them too
            print('Invalid row : '+line.rstrip('\n'))
        # end try/except
    # end for
    # return data records
    return output, nlines
# end def getDataFromFile

#
# ask for master file from user
masterFile = input("Please provide master file : ")

# read master file and extract data files
try:
    dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]
except:
    print("Impossible to read master file or invalid file name")
    exit(1)
# end try/except

# read data from data files
# we assume that the data files are accessible locally or we have the full path
#
# rawData is a list of 3 list which contains dictionaries with data from each file
rawData = [getDataFromFile(file) for file in dataFiles]

#
# given that we do not keep track of the file the data comes from
# we need to flatten the structure
uniqueListData = [item2 for item1 in rawData for item2 in item1[0]]
#
# the previous statment can be complicated and hard to understand
# it is equivalent to do the following:
# uniqueListData = [];
#  for item1 in rawData:
#     for item2 in item1:
#          uniqueListData.append(item2)
#      # end for item2
#  # end for item1
#

#
# number of files read
# this is equivalent to the number of elements in rawData
numberFiles = len(rawData)

#
# total number of lines read
# this is equivalent to the sum of the second item in each item of rawData
totalLines = sum([item[1] for item in rawData])

#
# total number distance run by every participant
# this is equivalent of the sum of the "distance" element of the items in the uniqueListdata
totalDistanceRun = sum([item['distance'] for item in uniqueListData])

#
# compute distance run for each participant and how many records we have for each one of them
# initialize all the accmulators
# dictionary with one element for each participant whose value is
# the list of all the distances found in data for the participant
participantDistances = {}

# loops on all the records
for item in uniqueListData:
    # check if the names has already been found previously or if it is new
    # if it is new, initialize elements in the accumulators
    if not item['name'] in participantDistances.keys():
        participantDistances[item['name']] = []
    # insert distance in the list for this participant
    participantDistances[item['name']].append(item['distance'])
# end for

# initialize accumulators
# distance run for each participant
participantDistanceRun = {}
# minum distance run with name
minDistance = { 'name' : None, 'distance': None }
# maximum distance run with name
maxDistance = { 'name' : None, 'distance': None }
# appearences dictionary
appearences = {}
#
# computes the total distance run for each participant iterating on all the participants
for name, values in participantDistances.items():
    # compute distance for current name / participant
    participantDistanceRun[name] = sum(values)
    # check if we need to update min
    # if this is the first iteration or if the current participant distance is lower than the current min
    if minDistance['name'] is None or minDistance['distance'] > participantDistanceRun[name]:
        minDistance['name'] = name
        minDistance['distance'] = participantDistanceRun[name]
    # end if
    # check if we need to update max
    # if this is the first iteration or if the current participant distance is lower than the current min
    if maxDistance['name'] is None or maxDistance['distance'] < participantDistanceRun[name]:
        maxDistance['name'] = name
        maxDistance['distance'] = participantDistanceRun[name]
    # end if
    #
    # appearences is equivalent to the length of the distances
    participantAppearences = len(values)
    #
    # check if we need to initialize this entry
    if not participantAppearences in appearences.keys():
        appearences[participantAppearences] = []
    appearences[participantAppearences].append(name)
# end for

#
# compute total number of participant
# this is equivalent to the length of the participantDistances
totalNumberOfParticipant = len(participantDistances);

#
#  compute total number of participants with more than one record
totalNumberOfParticipantWithMultipleRecords = 0;
for app, names in appearences.items():
    # skip participants with only one record
    if app == 1:
        continue
    # add number of participants with this number of records
    totalNumberOfParticipantWithMultipleRecords += len(names)
# end for

#
# set format strings
INTEGER = '5d'
FLOAT = '12.5f'
STRING = '20s'
#
# provide requested output
print("")
print(" Number of Input files read   : " + format(numberFiles,INTEGER))
print(" Total number of lines read   : " + format(totalLines,INTEGER))
print("")
print(" Total distance run           : " + format(totalDistanceRun,FLOAT))
print("")
print(" Max distance run             : " + format(maxDistance['distance'],FLOAT))
print("   by participant             : " + format(maxDistance['name'],STRING))
print("")
print(" Min distance run             : " + format(minDistance['distance'],FLOAT))
print("   by participant             : " + format(minDistance['name'],STRING))
print("")
print(" Total number of participants : " + format(totalNumberOfParticipant,INTEGER))
print(" Number of participants")
print("  with multiple records       : " + format(totalNumberOfParticipantWithMultipleRecords,FLOAT))
print("")

#
# create output file
outputFile = "f2016_cs8_man8_a3.output.csv"
# open file for writing
fh = open(outputFile,'w')
# write header in file
fh.write('name,records,distance\n')
# loop on all the participants
for name in participantDistanceRun.keys():
    # write line in file
    fh.write(','.join([name, str(len(participantDistances[name])), str(participantDistanceRun[name])]) + '\n')
#end for
# close files
fh.close()


