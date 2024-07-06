# Package Delivery Service
Package loading and delivery application that organizes packages on trucks based on delivery addresses. The program utilizes a hashmap data structure to store package information and a machine learning algorithm to organize and sort the packages on trucks with the most efficient route. The program is able to manipulate the datasets in the CSV files (adding, removing, updating aspects of package information) as needed. A "nearest neighbor" machine learning algorithm is used to organize packages.

SCENARIO:
A parcel service needs to determine an efficient route and delivery distribution for their daily local deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements that are listed in the attached CSV file.

Your task is to determine an algorithm, write a program, and present a solution where all 40 packages will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for all trucks. The specific delivery locations are shown on the attached 'addresses' CSV file and distances to each location are given in the attached 'distances' CSV file. The intent is to use the program for this specific location and also for many other cities in each state where the parcel service has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.
The supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the 'packages' CSV, including what has been delivered and at what time the delivery occurred.

An intuitive UI is used to easily navigate the program and select desired statistcal information by the user.

(Comments throughout project refelect parts of assignment rubric.)
