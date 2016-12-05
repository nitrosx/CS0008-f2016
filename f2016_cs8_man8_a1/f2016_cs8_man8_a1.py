#!/usr/local/bin/python3
#
#
# name       : Max Novelli
# email      : man8@pitt.edu
# date       : 2016/10/05
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# This is the coding for the first assignment for class CS8 f2016
#
# We are required to write an application which asks for which unit system the user would like to enter the quantities.
# Unit systems are Metric and USC
# Once the user has decided which units he/she would like to use, we ask for distance and gas used in the unit selected.
# we convert them to the other unit system.
# We also compute the gas consumption and provide a table with all the quantities required in the format provided by the client.
#
#

#
# define conversion values
MILES_TO_KILOMETERS = 1.60934
GALLONS_TO_LITERS = 3.78541

# we ask the user which system he/she would like to use
print("")
units = input("Please select which unit system you would like to use: metric (M,m, Metric, metric) or usc (U,u,USC,usc) : ")
# validate units
# we retain only the first letter and we conver it to lower case
units = units[0].lower()
if units != 'm' and units != 'u':
    print("Please re-run this application and select a valid unit system:")
    print(" - metric = M, m, Metric, metric")
    print(" - usc    = U, u, USC, usc).")
    exit()
#end if
print("")

# if we get here, the user should have selected valid units: m or u
#
# input values
# validate inputs
# convert values
if units == 'm':
    #
    # provide feedback to user about having selected metric
    print("You have selected metric units")
    print("")
    # the user selected to enter distance and gas in metric units
    # distance in km
    dm = float(input('Please enter the distance drive in km      : '))
    # gas used in liters
    gm = float(input('Please enter the gas amount used in liters : '))
    #
    # validate values entered
    # both distance and gas should be greater than 0
    if dm <= 0:
        print("Please enter a distance driven greater than 0. Thanks.")
        exit()
    #end if
    if gm <= 0:
        print("Please enter a gas amount greater than 0. Thanks.")
        exit()
    #end if
    #
    # convert metric to usc
    # distance in miles
    du = dm / MILES_TO_KILOMETERS
    # gas amount in gallons
    gu = gm / GALLONS_TO_LITERS

elif units == 'u':
    #
    # provide feedback to user about having selected metric
    print("You have selected usc units")
    print("")
    # the user selected to enter distance and gas in usc units
    # distance in miles
    du = float(input('Please enter the distance drive in miles    : '))
    # gas used in liters
    gu = float(input('Please enter the gas amount used in gallons : '))
    #
    # validate values entered
    # both distance and gas should be greater than 0
    if du <= 0:
        print("Please enter a distance driven greater than 0. Thanks.")
        exit()
    # end if
    if gu <= 0:
        print("Please enter a gas amount greater than 0. Thanks.")
        exit()
    # end if
    #
    # convert metric to usc
    # distance in miles
    dm = du * MILES_TO_KILOMETERS
    # gas amount in gallons
    gm = gu * GALLONS_TO_LITERS

else:
    #
    # we should never come here, given the input validation
    # just in case we keep the else, if anything happens
    print("Invalid units selected. Please ask for support")
    exit()
#end if

#
# here we should have both sidtance and gas amount in both metric and usc
# we proceed to compute gas consumption
#
# gas consumption in usc: miles per gallon
cu = du / gu
#
# gas consumption in metric: liters / 100 kilometers
cm = 100 * gm / dm

#
# here we rate the gas consumption
# rating is computed based on metric gas consumption
#
# initialize rating to something obviously wrong
cr = 'unknown'
# select rating
if cm > 20:
    cr = "Extremely poor"
elif cm > 15 and cm <= 20:
    cr = "Poor"
elif cm > 10 and cm <= 15:
    cr = "Average"
elif cm > 8  and cm <= 10:
    cr = "Good"
else:
    # this is the branch that is executed when cm <= 8
    cr = "Excellent"
#end if

#
# now we are ready to provide the output according the specs given by the client
# -------
#                                USC               Metric
# Distance ______________:    10.000 miles         16.093 Km
# Gas ___________________:     3.000 gallons       11.356 Liters
# Consumption ___________:     3.333 mpg           70.566 l/100Km
#
# Gas Consumption Rating : Extremely Poor
# --------

print("")
print("                                 USC               Metric")
print(" Distance ______________: ", format(du,'10.3f'), " miles     ", format(dm,'10.3f'), " km", sep="" )
print(" Gas ___________________: ", format(gu,'10.3f'), " gallons   ", format(gm,'10.3f'), " liters", sep="" )
print(" Consumption ___________: ", format(cu,'10.3f'), " mpg       ", format(cm,'10.3f'), " l/100km", sep="" )
print("")
print(" Gas Consumption Rating : ", cr, sep="")