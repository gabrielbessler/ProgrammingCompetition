class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odds = [x for x in A if x % 2 == 0]
        evens = [x for x in A if x % 2 == 1]
        return odds + evens 
