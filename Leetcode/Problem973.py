class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distances = []
        for point in points: 
           distances.append((point[0]**2 + point[1]**2, point))
            
        distances.sort()
        return [x[1] for x in distances[:K]]
