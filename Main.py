# Tyler Petrow
# ID: 011118169
# WGU C950 - Data Structures and Algorithms II
# NHP3 TASK 2: WGUPS ROUTING PROGRAM IMPLEMENTATION

import csv
import datetime

from Truck import Truck
from Package import Package
from hashmap import Hashmap

# read in distance CSV file
with open('distanceCSV.csv') as csvfile1:
    distanceInfo = csv.reader(csvfile1)
    distanceInfo = list(distanceInfo)

# read in address CSV file
with open('addressCSV.csv') as csvfile2:
    addressInfo = csv.reader(csvfile2)
    addressInfo = list(addressInfo)

# read in package CSV file
with open('packageCSV.csv') as csvfile3:
    packageInfo = csv.reader(csvfile3)
    packageInfo = list(packageInfo)


# loadPackageData will take a CSV file and a hashmap as input to method
def loadPackageData(filename, packageHash):
    with open(filename) as package_info:
        packageData = csv.reader(package_info)
        # for every row in the packageData CSV file, each column's values are stored in a new package
        for row in packageData:
            pkgID = int(row[0])
            pkgAddress = row[1]
            pkgCity = row[2]
            pkgState = row[3]
            pkgZipcode = row[4]
            pkgDeadline = row[5]
            pkgWeight = row[6]
            pkgStatus = "At Hub"

            # create new Package object from Package.py using package CSV file data for construction
            newPackage = Package(pkgID, pkgAddress, pkgCity, pkgState, pkgZipcode, pkgDeadline, pkgWeight, pkgStatus)

            # insert newPackage into hashtable, ID is key, package is value
            packageHash.insertion(pkgID, newPackage)


# loadDistanceData will take an x-value and y-value corresponding to x and y axis values on distance table CSV
def loadDistanceData(x_value, y_value):
    # assign distance to the x-y coordinate from distance CSV file
    distance = distanceInfo[x_value][y_value]
    if distance == '':  # repeated distance values are blank in the file, so flip y and x to get duplicate distance value
        distance = distanceInfo[y_value][x_value]

    return float(distance)


# loadAddressData takes an address (string) input and returns the integer value for the address
def loadAddressData(address):
        for row in addressInfo:
            if address in row[2]:
                return int(row[0])


# create hash table and fill it with packages from CSV file
packageHashmap = Hashmap()
loadPackageData("packageCSV.csv", packageHashmap)


# create truck objects and manually load packages with special notes in mind
truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 37, 39, 40], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=8))

truck2 = Truck(16, 18, None, [3, 6, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

truck3 = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 25, 28, 32, 33, 34], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))


# puts the truck out for delivery, will track distance driven and nearest neighbor algorithm is here to organize packages
def delivering(truck):
    #  all packages into array of not delivered
    notDelivered = []
    for packageID in truck.packages:

        package = packageHashmap.lookup(packageID)

        notDelivered.append(package)
    # clear the package list of a given truck so packages can be ordered and placed in order from algorithm
    truck.packages.clear()

    # iterate through the list of notDelivered until empty
    # adds nearest neighbor into truck.packages list one by one
    # main algorithm of project
    while len(notDelivered) > 0:
        next_address = 2000
        next_package = None
        for pkg in notDelivered:
            if loadDistanceData(loadAddressData(truck.address), loadAddressData(pkg.address)) <= next_address:
                next_address = loadDistanceData(loadAddressData(truck.address), loadAddressData(pkg.address))
                next_package = pkg
        truck.packages.append(next_package.ID)  # adds nearest neighbor into truck.packages list
        notDelivered.remove(next_package)  # removes nearest neighbor from notDelivered (indicating delivered)
        truck.mileage += next_address  # calculate the mileage between this address and next and compound into mileage
        truck.address = next_package.address  # updates truck's current address attribute to the package it drove to
        truck.time += datetime.timedelta(hours=next_address / 18)  # update total time between packages
        next_package.deliveryTime = truck.time
        next_package.departureTime = truck.departureTime


# truck 1 and truck 2 go out for delivery
delivering(truck1)
delivering(truck2)

# only two trucks go at a time. Truck 3 cannot go until 1 and 2 are back
truck3.departureTime = min(truck1.time, truck2.time)
delivering(truck3)


# main UI (menu) of program
class Main:
    # "menu" screen gives user 3 options to view
    print("Welcome to WGUPS Delivery Service Program")
    print("*****************************************")
    print("")
    print("Please select a menu option to view desired result")
    print("")
    print("1. View status of any single package at a certain time")
    print("")
    print("2. View status of all packages at a certain time")
    print("")
    print("3. View package ID's loaded onto respective trucks")
    print("")
    print("4. View total mileage travelled by individual truck")
    print("")
    print("5. View total mileage travelled by all trucks")
    print("")

    menuChoice = input("Enter choice: ")
    if menuChoice == "1":  # user wants to view a single package status at a specific time
        try:
            # user will be asked for a specific time
            print("*************************************************************************")
            userTime = input("Please enter a time to check status of package(s).(HH:MM:SS): ")
            (h, m, s) = userTime.split(":")
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # user asked which package ID to check status of at that time
            choiceID = input("Enter the package ID of the package you'd like to track at (" + userTime + "): ")
            package = packageHashmap.lookup(int(choiceID))
            package.updateStatus(convert_timedelta)
            print(str(package))
        except ValueError:  # if user does not enter correct time format, exit
            print("Entry invalid. Closing program.")
            exit()

    elif menuChoice == "2":  # user wants to view all package statuses at a specific time
        try:
            print("*************************************************************************")
            userTime = input("Please enter a time to check status of package(s).(HH:MM:SS): ")
            (h, m, s) = userTime.split(":")
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # iterate through all packages and print each
            for packageID in range(1, 41):
                package = packageHashmap.lookup(packageID)
                package.updateStatus(convert_timedelta)
                print(str(package))
        except ValueError:  # if user does not enter correct time format, exit
            print("Entry invalid. Closing program.")
            exit()

    elif menuChoice == "3":  # user wants to view package ID's loaded onto their respective trucks
        print("*************************************************************************")
            # print each truck's packageIDs
        print("Truck 1 Package ID's: " + str(truck1.packages))
        print("Truck 2 Package ID's: " + str(truck2.packages))
        print("Truck 3 Package ID's: " + str(truck3.packages))

    elif menuChoice == "4":  # user wants to view total mileage of a specific truck
        print("*************************************************************************")
        userTruck = input("See mileage for which truck number? (1, 2, or 3): ")
        if userTruck == "1":
            print("The mileage for truck 1 is: " + str(truck1.mileage))
        elif userTruck == "2":
            print("The mileage for truck 2 is: " + str(truck2.mileage))
        elif userTruck == "3":
            print("The mileage for truck 3 is: " + str(truck3.mileage))
        else:
            print("Entry invalid. Closing program.")
            exit()

    elif menuChoice == "5":  # user wants to view total truck mileage
        print("*************************************************************************")
        print("The mileage for truck 1 is: " + str(truck1.mileage))
        print("The mileage for truck 2 is: " + str(truck2.mileage))
        print("The mileage for truck 3 is: " + str(truck3.mileage))
        print("Total Mileage for all trucks: ")
        print(truck1.mileage + truck2.mileage + truck3.mileage)

    else:  # if user does not enter 1, 2, 3, 4, or 5 from main menu, exit program
        print("Entry invalid. Closing program.")
        exit()
