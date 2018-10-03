class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        L = [] 
        for i in range(left, right + 1): 
            s = str(i)
            self_dividing = True 
            for digit in s: 
                if int(digit) == 0 or i % int(digit) != 0:
                    self_dividing = False 
                    break 
            if self_dividing: 
                L.append(int(s))
        return L
            