class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.hashMap = collections.defaultdict(int)
        
        

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.hashMap[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        #print self.hashMap
        for num in self.hashMap:
            if value - num in self.hashMap and (num != value - num or self.hashMap[num] > 1):
                return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)