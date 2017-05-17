import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.positions = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.positions.keys():
            return False
        else:
            self.items.append(val)
            self.positions[val] = len(self.items)-1
            return True            

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.positions.keys():
            last_item = self.items.pop()
            position = self.positions.pop(val)
            if position != len(self.items):
                self.items[position] = last_item
                self.positions[last_item] = position
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.items) == 0:
            return 
        else:
            return random.choice(self.items)        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
