# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Recursive solution for searchBST 
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # Base Case 
        if (root.val == val): 
            return root 
        
        # Look in left subtree 
        if (val < root.val): 
            if (root.left == None): 
                return None
            return self.searchBST(root.left, val)
        
        # Look in right subtree 
        if (root.right == None): 
            return None
        return self.searchBST(root.right, val)

    # Non-recursive Solution: 
    
    def searchBSTNonRecursive(self, root, val): 
        while root != None: 
            if root.val == val: 
                return val
            elif val < root.val: 
                root = root.left 
            elif val > root.val: 
                root = root.right
        return None