class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        type = None 
        for i in range(len(A) - 1): 
            if A[i] < A[i + 1]:
                if type == 2: 
                    return False 
                type = 1
            elif A[i] > A[i + 1]:
                if type == 1: 
                    return False
                type = 2
        return True