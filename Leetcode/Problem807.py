class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # Get max value in each row and column 
        maxRows = [0] * len(grid)
        maxCols = [0] * len(grid[0])
        for row in range(0, len(grid)):
            maxRows[row] = max(grid[row])
            for col in range(0, len(grid[row])): 
                maxCols[col] = max(maxCols[col], grid[row][col])

        # Now, each [i][j] can be equal to min of its rowMax/colMax
        total = 0
        for row in range(0, len(grid)): 
            for col in range(0, len(grid[row])):
                total += min(maxRows[row], maxCols[col]) - grid[row][col]

        return total

