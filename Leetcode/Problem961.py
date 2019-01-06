class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # If there are N + 1 unique elements and one is repeated 
        #   N times, then every other element only shows up once 
        #   Therefore as soon as we find an element twice we are 
        #   done.

        # This is O(N) in space and time complexity 
        s = set() 
        for el in A: 
            if el in s: 
                return el 

            s.add(el) 