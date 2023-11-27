from typing import Optional
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


class Solution:
    # sol 1, recursive
    # time O(n * m), space O(n * m)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSametree(t1: Optional[TreeNode], t2: Optional[TreeNode]):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False

            return isSametree(t1.left, t2.left) and isSametree(t1.right, t2.right)

        def _isSubtree(root, subRoot):
            if not root:
                return False

            return (
                isSametree(root, subRoot)
                or _isSubtree(root.left, subRoot)
                or _isSubtree(root.right, subRoot)
            )

        return _isSubtree(root, subRoot)


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(17)

    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(17)

    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    root3 = TreeNode()
    root4 = None

    root5 = TreeNode(3)
    root5.left = TreeNode(4)
    root5.right = TreeNode(5)
    root5.left.left = TreeNode(1)
    root5.left.right = TreeNode(2)

    root6 = TreeNode(4)
    root6.left = TreeNode(1)
    root6.right = TreeNode(2)

    # printTree(root)
    print(solution.isSubtree(root5, root6))
    # print(solution.isSubtree(root4, root3))
