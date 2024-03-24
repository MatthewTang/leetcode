from typing import Optional, List
from collections import deque
import unittest

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        # Check if 'other' is an instance of TreeNode
        if not isinstance(other, TreeNode):
            return False
        # Compare the current node's value
        if self.val != other.val:
            return False
        # Recursively compare the left subtree
        if self.left or other.left:
            if not self.left or not other.left:
                return False
            if not self.left == other.left:
                return False
        # Recursively compare the right subtree
        if self.right or other.right:
            if not self.right or not other.right:
                return False
            if not self.right == other.right:
                return False
        # If all checks pass, the trees are equal
        return True

    def __repr__(self) -> str:
        return f"{self.val}"


def printTree(root: TreeNode, level=0):
    if root is None:
        return
    printTree(root.right, level + 1)
    print("\t" * level, root.val)
    printTree(root.left, level + 1)


class Solution:
    def preorder(self, root: Optional[TreeNode]):
        def t(node: Optional[TreeNode]):
            if not node:
                return
            print(node.val)
            t(node.left)
            t(node.right)

        t(root)

    def inorder(self, root: Optional[TreeNode]):
        def t(node: Optional[TreeNode]):
            if not node:
                return
            t(node.left)
            print(node.val)
            t(node.right)

        t(root)

    def postorder(self, root: Optional[TreeNode]):
        def t(node: Optional[TreeNode]):
            if not node:
                return
            t(node.left)
            t(node.right)
            print(node.val)

        t(root)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def findSums(curr: Optional[TreeNode], out: List[int]):
            if not curr:
                return 0

            leftSum = findSums(curr.left, out)
            rightSum = findSums(curr.right, out)

            maxSum = max(
                curr.val,
                curr.val + leftSum,
                curr.val + rightSum,
            )

            # global max
            out.append(maxSum)
            # local max
            out.append(curr.val + leftSum + rightSum)

            return maxSum

        out = []
        findSums(root, out)

        print(out)
        return max(out)


class TestSolution(unittest.TestCase):
    def test1(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        s = Solution()
        self.assertEqual(s.maxPathSum(root1), 6)

    def test2(self):
        root1 = TreeNode(-10)
        root1.left = TreeNode(9)
        root1.right = TreeNode(20)
        root1.right.left = TreeNode(15)
        root1.right.right = TreeNode(7)
        s = Solution()
        self.assertEqual(s.maxPathSum(root1), 42)

    def test3(self):
        root1 = TreeNode(2)
        root1.left = TreeNode(-1)
        s = Solution()
        self.assertEqual(s.maxPathSum(root1), 2)

    # WIP
    def test4(self):
        root1 = TreeNode(5)
        root1.left = TreeNode(4)
        root1.right = TreeNode(8)
        root1.left.left = TreeNode(11)
        root1.right.left = TreeNode(13)
        root1.right.right = TreeNode(4)
        root1.left.left.left = TreeNode(7)
        root1.left.left.right = TreeNode(2)
        root1.right.right.right = TreeNode(1)
        s = Solution()
        self.assertEqual(s.maxPathSum(root1), 48)


if __name__ == "__main__":
    unittest.main()
