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
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    printTree(root)
    print("====================================")
    printTree(solution.invertTree(root))
