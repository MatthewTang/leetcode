from typing import Optional
from collections import deque

# insight: Binary Search Tree
# BST property, means that the left subtree is less than the root, and the right subtree is greater than the root


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


class Solution:
    # sol 1, recursive
    # time O(n), since worst case we need to traverse all nodes
    # space O(n), since we are using recursion
    # def lowestCommonAncestor(
    #     self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    # ) -> "TreeNode":
    #     def fn(tree, p, q, res):
    #         if len(res) > 0:
    #             return
    #
    #         if not tree:
    #             return
    #
    #         if fn(tree.left, p, q, res) and fn(tree.right, p, q, res):
    #             res.append(tree)
    #             return
    #
    #         if fn(tree.left, p, q, res) or fn(tree.right, p, q, res):
    #             if tree.val == p.val or tree.val == q.val:
    #                 res.append(tree)
    #                 return
    #
    #             return True
    #
    #         return tree.val == p.val or tree.val == q.val
    #
    #     res = []
    #     fn(root, p, q, res)
    #
    #     print("res::", res)
    #
    #     return res[0] if len(res) > 0 else None

    # sol 2, iterative, BST
    # time O log(n), since we are traversing only one branch
    # space O(1)
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while True:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = root.right
    q = root.left.right.left

    printTree(root)
    print(solution.lowestCommonAncestor(root, p, q))
