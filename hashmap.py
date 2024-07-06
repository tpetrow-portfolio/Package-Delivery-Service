# Create hashmap class with needed attributes and functions for assignment

#Source: Python: Creating a HASHMAP using Lists video by Oggi AI - Artificial Intelligence Today
#Acquired from C950 Course Resources and Zybooks

class Hashmap:
    # initialize starting array and empty each position
    def __init__(self):
        self.map = []
        for i in range(40):
            self.map.append([])

    # function takes a key and a value and assigns the hash position with the value
    def insertion(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        hashKey = hash(key) % len(self.map)
        bucketList = self.map[hashKey]

        # update key if it is already in the bucket
        for pair in bucketList:
            # print (key_value)
            if pair[0] == key:
                pair[1] = item
                return True

        # if not, insert the item to the end of the bucket list
        keyValue = [key, item]
        bucketList.append(keyValue)
        return True

    # delete value at hash location
    def delete(self, key):
        hashkey = hash(key) % len(self.map)

        if self.map[hashkey] is None:  # if bucket at hash location is empty
            return False
        else:
            for i in range(0, len(self.map[hashkey])):  # looks for key in bucket
                if self.map[hashkey][i][0] == key:
                    self.map[hashkey].pop(i)

    # searches for an item with a matching key in the hashtable. Returns the item if found, or None if not found.
    def lookup(self, key):
        hashKey = hash(key) % len(self.map)
        bucketList = self.map[hashKey]
        for pair in bucketList:
            if key == pair[0]: # if key matches pair
                return pair[1]
        return None # if no key found, return none