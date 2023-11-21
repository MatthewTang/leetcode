from typing import Optional


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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def countD(root: Optional[TreeNode], d: int):
            if not root:
                return d

            return max(countD(root.left, d + 1), countD(root.right, d + 1))

        return countD(root, 0)


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(17)

    root2 = TreeNode(1)
    root2.right = TreeNode(2)

    root3 = TreeNode()
    root4 = None

    # printTree(root)

    print(solution.maxDepth(root))
    print(solution.maxDepth(root2))
    print(solution.maxDepth(root3))
    print(solution.maxDepth(root4))
