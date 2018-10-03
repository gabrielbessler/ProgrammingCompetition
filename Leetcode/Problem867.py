class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[x][row_index] for x in range(len(A))] for row_index in range(len(A[0]))]