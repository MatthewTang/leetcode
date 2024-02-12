from typing import Optional, List
from collections import deque
import unittest


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
    # time complexity: O(n^2), bc n -> n-1 -> n-2 -> ... -> 1  ,  O(n) for each iteration bc of the index() method
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def fn(preorder: List[int], inorder: List[int]):
            # base case
            if len(preorder) == 0:
                return None

            node_val = preorder[0]
            ind = inorder.index(node_val)  # O(n)
            left = inorder[:ind]
            right = inorder[ind + 1 :]

            node = TreeNode(node_val)
            node.left = fn(preorder[1 : 1 + len(left)], left)
            node.right = fn(preorder[1 + len(left) :], right)

            return node

        return fn(preorder, inorder)

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


class TestSolution(unittest.TestCase):
    def test1(self):
        root1 = TreeNode(3)
        root1.left = TreeNode(1)
        root1.right = TreeNode(4)
        root1.left.right = TreeNode(2)

        # root2 = TreeNode(5)
        # root2.left = TreeNode(3)
        # root2.right = TreeNode(6)
        # root2.left.left = TreeNode(2)
        # root2.left.right = TreeNode(4)
        # root2.left.left.left = TreeNode(1)

        # root3 = TreeNode(3)
        # root3.left = TreeNode(9)
        # root3.right = TreeNode(20)
        # root3.right.left = TreeNode(15)
        # root3.right.right = TreeNode(7)

        # printTree(root3)

        # solution = Solution()
        # solution.preorder(root3)
        # solution.inorder(root3)
        # solution.postorder(root3)

        solution = Solution()
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        tree = solution.buildTree(preorder, inorder)

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(tree, root)

    def test2(self):
        solution = Solution()
        preorder = [-1]
        inorder = [-1]
        tree = solution.buildTree(preorder, inorder)
        root = TreeNode(-1)
        self.assertEqual(tree, root)

    def test3(self):
        solution = Solution()
        preorder = [1, 2]
        inorder = [2, 1]
        tree = solution.buildTree(preorder, inorder)
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(tree, root)


if __name__ == "__main__":
    unittest.main()
