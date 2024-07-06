# Create Truck class with needed attributes

class Truck:
    def __init__(self, maxPkg, speed, load, packages, mileage, address, departureTime):
        self.maxPkg = maxPkg
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departureTime = departureTime
        self.time = departureTime

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.maxPkg, self.speed, self.load,
                                               self.packages, self.mileage, self.address, self.departureTime)