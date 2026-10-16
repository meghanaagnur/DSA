class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        tree = [root]
        while (tree):
            x = tree.pop(0)
            if x == None:
                continue
            temp = x.left
            x.left = x.right
            x.right = temp
            tree.append(x.left)
            tree.append(x.right)
        return root