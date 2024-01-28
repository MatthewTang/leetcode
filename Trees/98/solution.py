from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val}"


def printTree(root: TreeNode, level=0):
    if root is None:
        return
    printTree(root.right, level + 1)
    print("\t" * level, root.val)
    printTree(root.left, level + 1)


# Given `root` of a bin tree, determine if it is a valid binary search tree (BST)
# valid BST is defined as follows:
# - the left subtree of a node contains only nodes with keys less than the node's key
# - the right subtree of a node contains only nodes iwth keys greater than the node's key
# - both the left and right subtree must also be binary search tree.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # def retMinMax(node: Optional[TreeNode]):
        #     if not node:
        #         return float("infinity"), -float("infinity")
        #
        #     rmin, rmax = retMinMax(node.right)
        #     if not rmin > node.val:
        #         return -float("infinity"), float("infinity")
        #
        #     lmin, lmax = retMinMax(node.left)
        #     if not lmax < node.val:
        #         return -float("infinity"), float("infinity")
        #
        #     return min(node.val, lmin), max(node.val, rmax)
        #
        # l, r = retMinMax(root)
        # print(l, r)
        # return not l == -float("infinity")

        # neetcode sol
        def valid(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)

    root3 = TreeNode(5)
    root3.left = TreeNode(4)
    root3.right = TreeNode(6)
    root3.right.left = TreeNode(3)
    root3.right.right = TreeNode(7)
    root3.left.left = TreeNode(2)
    root3.left.right = TreeNode(6)

    roots = [root, root2, root3]

    for root in roots:
        print("---------------------------------------")
        printTree(root)
        print(solution.isValidBST(root))
