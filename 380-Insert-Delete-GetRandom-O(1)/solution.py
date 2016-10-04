class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        self.isListValid = True

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.dict[val] = True
            self.list.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        else:
            del self.dict[val]
            self.isListValid = False
            return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        temp = None
        if len(self.dict):
            if not self.isListValid:
                self.list = self.dict.keys()
                self.isListValid = True
            temp = random.choice(self.list)
        return temp

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()