# Create Package class with needed attributes and updateStatus function
import datetime

class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departureTime = None
        self.deliveryTime = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.deadline, self.weight, self.deliveryTime,
                                                       self.status)

    # updateStatus function takes timedelta from main to see if package delivery time is before or after current time
    # indicates whether the package has been delivered, en route, or still at hub
    
    def updateStatus(self, convert_timedelta):
        # if current time is greater than 10:20, update package ID 9 with new address and zipcode
        if convert_timedelta >= datetime.timedelta(hours=10, minutes=20) and self.ID == 9:
            self.address = "410 S State St"
            self.zipcode = 84111
        if self.deliveryTime < convert_timedelta:
            self.status = "Delivered"
        elif self.departureTime > convert_timedelta:
            self.status = "En Route"
        else:
            self.status = "At Hub"
