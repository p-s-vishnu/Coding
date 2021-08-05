"""
parent_idx = int(index-1/2), where index > 0
left_child_idx = 2*parent_idx + 1
right_child_idx = 2*parent_idx + 2


112.Path Sum 1
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def has_path_sum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        val = root.val
        if root.left is None and root.right is None:
            return val == sum
        return self.hasPathSum(root.left, sum - val) or self.hasPathSum(root.right, sum -val)


"""
113.Path Sum 2
"""
from typing import List
class Solution:
    def path_sum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        if root is None:
            return []
        if root.left is None and root.right is None and target_sum - root.val == 0:
            return [[root.val]]
        l = self.pathSum(root.left, target_sum - root.val)
        r = self.pathSum(root.right, target_sum - root.val)
        return [[root.val] + elem for elem in l+r]
        