class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        num_lines = 1
        curr_width = 0
        for letter in S: 
            index = ord(letter) - 97 
            if widths[index] + curr_width > 100: 
                num_lines += 1 
                curr_width = widths[index] 
            else: 
                curr_width += widths[index] 
                
        return num_lines, curr_width 
