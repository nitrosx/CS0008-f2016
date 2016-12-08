#
#
# name       : Max Novelli
# email      : man8@pitt.edu
# date       : 2016/10/31
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Final Project
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
# In this program, the student should make the best use of everything that has learn so far in this class,
# reuse as much as he/she can from assignment #3, improve upon it and he/she has to use a class named participants
# that has 3 properties:
# - name: name of the participant. String.
# - distance: accumulator for total distance run by the participant. Float.
# - runs: accumulator for the total number of runs run by the participant.
#
# and, at least, the following methods:
# - addDistance(d)
#   add single distance to the distance accumulator and increments runs by 1. Argument d is a single float.
# - addDistances(ld)
#   add an array of distances to distance accumulator. Argument ld is a list of floats. getDistance()
#   get the current value of the distance accumulator.
# - getName()
#   get the name of the participant of the current instance
# - getDistance()
#   get the total distance run computed
# - getRuns()
#   get the total number of runs
# - __init__ (n,d=0)
#   initializer method. set name and initial distance if provided. If initial distance is not specified,
#   it should be set to zero
# - __str__()
#   stringify method. Returns a string with name, total distance run and how many distances the object added,
#   according to the following format:
#   Name : xxxxxxxxxxxxxxxxxxx. Distance run : yyyy.yyyy. Runs : zzzz
#
#   where xxxxxxxxxxxxxxxxxxx is a right align string of 20 characters for the name,
#   yyyy.yyyy is the total distance run with 9 digits, decimal point and 4 decimals,
#   and zzzz is the number of runs with 4 digits, no decimals.
#

#
# class participant definition according to specs from header
# class definition
class participant:
    """ participant class"""

    # properties
    # name of the participant
    name = "unknown"
    # total distance run by the participant
    distance = 0
    # total number of runs by the participant
    runs = 0

    # methods
    # initializer methods
    def __init__(self, name, distance=0):
        # set name
        self.name = name
        # set distance if non zero
        if distance > 0:
            # set distance
            self.distance = distance
            # set number of runs accordingly
            self.runs = 1
            # end if

    # end def __init__

    # addDistance method
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
            # end if

    # end def addDistance

    # addDistances method
    def addDistances(self, distances):
        # loops over list
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
                # end if
                # end for

    # end def addDistance

    # return the name of the participant
    def getName(self):
        return self.name

    # end def getName

    # return the total distance run computed
    def getDistance(self):
        return self.distance

    # end def getDistance

    # return the number of runs
    def getRuns(self):
        return self.runs

    # end def getRuns

    # stringify the object
    def __str__(self):
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.runs, '4d')
        # end def __init__

    # convert to csv
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])
    # end def tocsv

# end class participant


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
def getDataFromFile(file):
    # initialize output list
    output = []
    # read file line by line
    for line in open(file,'r'):
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
    return output
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
# rawData is a list of all the records from each data file
# according to posting #43 of http://stackoverflow.com/questions/4344017/how-can-i-get-the-concatenation-of-two-lists-in-python-without-modifying-either
# sum() can concatenate lists in a list if it is provided with an empty list as initial value
rawData = sum([getDataFromFile(file) for file in dataFiles],[])
#
# the previous statement can be complicated and hard to understand
# it is equivalent to do the following:
# rawData = [];
# for file in dataFiles:
#    for item2 in getDataFromFile(file):
#       rawData.append(item2)
#    # end for item2
# # end for file
#
# or:
# rawData = [];
# for file in dataFiles:
#    rawData.extend(getDataFromFile(file))
# # end for file

#
# number of files read
# this is equivalent to the number of elements in dataFiles
numberFiles = len(dataFiles)

#
# total number of lines read
# this is equivalent to the sum of the second item in each item of rawData
totalLines = len(rawData)

#
# total number distance run by every participant
# this is equivalent of the sum of the "distance" element of the items in the uniqueListdata
totalDistanceRun = sum([item['distance'] for item in rawData])

#
# compute distance run for each participant and how many records we have for each one of them
# initialize all the accmulators
# dictionary with one element for each participant whose value is
# the list of all the distances found in data for the participant
participants = {}

# loops on all the records
for item in rawData:
    # check if the names has already been found previously or if it is new
    # if it is new, initialize elements in the accumulators
    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
    # insert distance in the list for this participant
    participants[item['name']].addDistance(item['distance'])
# end for

# initialize accumulators
# minum distance run with name
minDistance = { 'name' : None, 'distance': None }
# maximum distance run with name
maxDistance = { 'name' : None, 'distance': None }
# appearences dictionary
apparences = {}
#
# computes the total distance run for each participant iterating on all the participants
for name, object in participants.items():
    # get the total distance run by this participant
    distance = object.getDistance()
    # check if we need to update min
    # if this is the first iteration or if the current participant distance is lower than the current min
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance
    # end if
    # check if we need to update max
    # if this is the first iteration or if the current participant distance is lower than the current min
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance
    # end if
    #
    # get number of runs, aka apparences from participant object
    participantAppearences = object.getRuns()
    #
    # check if we need to initialize this entry
    if not participantAppearences in apparences.keys():
        apparences[participantAppearences] = []
    apparences[participantAppearences].append(name)
# end for

#
# compute total number of participant
# this is equivalent to the length of the participantDistances
totalNumberOfParticipant = len(participants);

#
# compute total number of participants with more than one record
# extract all the participants that have 2 or more runs
# and count th enumber of elements in the list with len()
totalNumberOfParticipantWithMultipleRecords = len([1 for item in participants.values() if item.getRuns() > 1])

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
for name, object in participants.items():
    # write line in file
    fh.write(object.tocsv() + '\n')
#end for
# close files
fh.close()


